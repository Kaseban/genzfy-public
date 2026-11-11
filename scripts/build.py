#!/usr/bin/env python3
"""Check and package the Genzfy skill pack.

    python3 scripts/build.py check       validate skills and cross-references
    python3 scripts/build.py claude-ai   dist/claude-ai/<skill>.zip, one upload per skill
    python3 scripts/build.py chatgpt     dist/chatgpt/ instructions + knowledge files
    python3 scripts/build.py all         all of the above

Standard library only, so it runs anywhere Python 3.9+ does.
"""

import re
import shutil
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
DIST = ROOT / "dist"
GPT_TEMPLATE = ROOT / "platforms" / "chatgpt" / "instructions.md"

# Custom GPT limits, as documented by OpenAI.
GPT_INSTRUCTIONS_MAX = 8000
GPT_KNOWLEDGE_MAX_FILES = 20
# Claude skill frontmatter limits.
NAME_MAX = 64
DESCRIPTION_MAX = 1024

REF = re.compile(r"(?:\.\./)*(?:[A-Za-z0-9_-]+/)?references/[A-Za-z0-9_-]+\.md")


def skill_dirs():
    return sorted(p for p in SKILLS.iterdir() if (p / "SKILL.md").is_file())


def read(path):
    # Explicit UTF-8 and LF so the build behaves the same on Windows (cp1252, CRLF checkouts).
    return path.read_text(encoding="utf-8").replace("\r\n", "\n")


def frontmatter(text):
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None
    fields = {}
    for line in m.group(1).splitlines():
        if line[:1].isspace():
            continue  # continuation of a multi-line value; check() rejects block scalars below
        key, _, value = line.partition(":")
        fields[key.strip()] = value.strip()
    return fields


def resolve(ref, md_file, skill_dir):
    """A reference is valid relative to the file that names it or to its skill's root.

    The SKILL.md files write paths from the skill root; workforce-patterns.md writes its
    one path from its own directory. Both conventions are in use, so both are accepted.
    """
    for base in (md_file.parent, skill_dir):
        target = (base / ref).resolve()
        if target.is_file():
            return target
    return None


def references(skill_dir):
    """Yield (md_file, ref, target) for every reference path in a skill."""
    for md in sorted(skill_dir.rglob("*.md")):
        for ref in sorted(set(REF.findall(read(md)))):
            yield md, ref, resolve(ref, md, skill_dir)


def check():
    errors = []
    dirs = skill_dirs()
    for d in dirs:
        text = read(d / "SKILL.md")
        fm = frontmatter(text)
        if fm is None:
            errors.append(f"{d.name}/SKILL.md: no frontmatter")
            continue
        if fm.get("name") != d.name:
            errors.append(f"{d.name}/SKILL.md: name '{fm.get('name')}' does not match directory")
        if len(fm.get("name", "")) > NAME_MAX:
            errors.append(f"{d.name}/SKILL.md: name over {NAME_MAX} characters")
        desc = fm.get("description", "")
        if not desc:
            errors.append(f"{d.name}/SKILL.md: missing description")
        elif len(desc) > DESCRIPTION_MAX:
            errors.append(f"{d.name}/SKILL.md: description is {len(desc)} chars, max {DESCRIPTION_MAX}")
        if desc in (">", ">-", "|", "|-"):
            errors.append(f"{d.name}/SKILL.md: multi-line description, write it on one line")
        elif "<" in desc or ">" in desc:
            errors.append(f"{d.name}/SKILL.md: angle brackets in description")
        for md, ref, target in references(d):
            if target is None:
                errors.append(f"{md.relative_to(ROOT)}: '{ref}' does not resolve")
    if errors:
        print("check failed:")
        for e in errors:
            print("  " + e)
        return False
    print(f"check ok: {len(dirs)} skills, all references resolve")
    return True


def home_skill(target):
    """The skill directory a shared file belongs to, for resolving its own references."""
    rel = target.relative_to(SKILLS.resolve())
    return SKILLS.resolve() / rel.parts[0]


def file_refs(md, skill_dir):
    for ref in sorted(set(REF.findall(read(md)))):
        yield resolve(ref, md, skill_dir)


def vendored(skill_dir):
    """Map each file outside this skill that it needs, directly or through another vendored
    file's references, to the name it gets inside it."""
    own_root = skill_dir.resolve()
    out = {}
    queue = [(md, skill_dir) for md in sorted(skill_dir.rglob("*.md"))]
    while queue:
        md, base = queue.pop()
        for target in file_refs(md, base):
            if target and own_root not in target.parents and target not in out:
                out[target] = target.name
                queue.append((target, home_skill(target)))
    names = list(out.values())
    dupes = sorted({n for n in names if names.count(n) > 1})
    if dupes:
        sys.exit(f"{skill_dir.name}: two shared files would both be vendored as {dupes}")
    return out


def rewrite_refs(text, md_file, skill_dir, mapping):
    """Point references at their location inside a self-contained bundle.

    mapping takes a resolved target file to the path it should be written as.
    """
    def sub(m):
        target = resolve(m.group(0), md_file, skill_dir)
        return mapping.get(target, m.group(0)) if target else m.group(0)
    return REF.sub(sub, text)


def build_claude_ai():
    """One zip per skill. claude.ai installs each skill in isolation, so the sibling paths
    (../genzfy/references/...) that work in Claude Code would point nowhere. Each zip carries
    its own copy of the shared files under references/ and its paths are rewritten to match.
    """
    out = DIST / "claude-ai"
    shutil.rmtree(out, ignore_errors=True)
    out.mkdir(parents=True)
    for d in skill_dirs():
        extra = vendored(d)
        own = {p.resolve() for p in d.rglob("*.md")}
        clash = set(extra.values()) & {p.name for p in (d / "references").glob("*.md")}
        if clash:
            sys.exit(f"{d.name}: vendored file would overwrite its own {sorted(clash)}")
        mapping = {t: f"references/{n}" for t, n in extra.items()}
        mapping.update({p: str(p.relative_to(d.resolve())) for p in own})
        with zipfile.ZipFile(out / f"{d.name}.zip", "w", zipfile.ZIP_DEFLATED) as z:
            for md in sorted(d.rglob("*.md")):
                z.writestr(f"{d.name}/{md.relative_to(d)}", rewrite_refs(read(md), md, d, mapping))
            for target, name in sorted(extra.items()):
                # A vendored file's own references are written from its home skill's root.
                text = rewrite_refs(read(target), target, home_skill(target), mapping)
                z.writestr(f"{d.name}/references/{name}", text)
        print(f"  dist/claude-ai/{d.name}.zip" + (f"  (+ {', '.join(sorted(extra.values()))})" if extra else ""))


def build_chatgpt():
    """Instructions plus a flat set of knowledge files. A Custom GPT has no directories, so
    every file is renamed to a unique flat name and every reference is rewritten to that name.
    """
    out = DIST / "chatgpt"
    shutil.rmtree(out, ignore_errors=True)
    (out / "knowledge").mkdir(parents=True)

    files = {}
    for d in skill_dirs():
        files[(d / "SKILL.md").resolve()] = (f"skill-{d.name}.md", d)
        for ref in sorted((d / "references").glob("*.md")):
            files[ref.resolve()] = (ref.name, d)
    names = [n for n, _ in files.values()]
    dupes = {n for n in names if names.count(n) > 1}
    if dupes:
        sys.exit(f"knowledge file names collide: {sorted(dupes)}")
    if len(files) > GPT_KNOWLEDGE_MAX_FILES:
        sys.exit(f"{len(files)} knowledge files, Custom GPT max is {GPT_KNOWLEDGE_MAX_FILES}")

    mapping = {t: f"{n} (knowledge file)" for t, (n, _) in files.items()}
    for target, (name, d) in sorted(files.items(), key=lambda kv: kv[1][0]):
        (out / "knowledge" / name).write_text(rewrite_refs(read(target), target, d, mapping), encoding="utf-8")

    instructions = read(GPT_TEMPLATE)
    if len(instructions) > GPT_INSTRUCTIONS_MAX:
        sys.exit(f"instructions are {len(instructions)} chars, Custom GPT max is {GPT_INSTRUCTIONS_MAX}")
    (out / "instructions.md").write_text(instructions, encoding="utf-8")
    print(f"  dist/chatgpt/instructions.md  ({len(instructions)} / {GPT_INSTRUCTIONS_MAX} chars)")
    print(f"  dist/chatgpt/knowledge/  ({len(files)} files)")


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else "all"
    if cmd not in ("check", "claude-ai", "chatgpt", "all"):
        sys.exit(__doc__)
    if not check():
        sys.exit(1)
    if cmd in ("claude-ai", "all"):
        build_claude_ai()
    if cmd in ("chatgpt", "all"):
        build_chatgpt()


if __name__ == "__main__":
    main()
