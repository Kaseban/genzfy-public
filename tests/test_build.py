"""Packaging and source-integrity checks, not generated-advice validation.

Run behavioral cases separately with real generated outputs; see fixtures/README.md.
"""
import importlib.util
import re
import tempfile
import unittest
import zipfile
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('genzfy_build', ROOT / 'scripts/build.py')
build = importlib.util.module_from_spec(spec)
spec.loader.exec_module(build)
LOCAL_LINK = re.compile(r'\[[^\]]*\]\(([^)]+\.md)(?:#[^)]*)?\)')


class SourceChecks(unittest.TestCase):
    def test_seven_valid_skills(self):
        self.assertEqual(len(build.skill_dirs()), 7)
        self.assertTrue(build.check())

    def test_pattern_ids_and_claim_records(self):
        patterns = build.read(build.SKILLS / 'genzfy/references/patterns.md')
        ledger = build.read(build.SKILLS / 'genzfy/references/claim-ledger.md')
        self.assertEqual(set(re.findall(r'^### (P\d\d) ', patterns, re.M)),
                         {f'P{i:02}' for i in range(1, 17)})
        self.assertEqual(set(re.findall(r'^## (C\d\d)\b', ledger, re.M)),
                         {f'C{i:02}' for i in range(1, 17)})
        for claim in re.findall(r'claim-ledger\.md#(c\d\d)', patterns):
            self.assertIn(f'## {claim.upper()}', ledger)

    def test_repo_markdown_links_resolve(self):
        for folder in ('skills', 'fixtures', 'platforms'):
            for path in (ROOT / folder).rglob('*.md'):
                for link in LOCAL_LINK.findall(build.read(path)):
                    if '://' not in link:
                        self.assertTrue((path.parent / link).is_file(), (path, link))


class BundleChecks(unittest.TestCase):
    def test_each_claude_bundle_has_dependency_closure(self):
        with tempfile.TemporaryDirectory() as tmp, patch.object(build, 'DIST', Path(tmp)):
            build.build_claude_ai()
            archives = sorted((Path(tmp) / 'claude-ai').glob('*.zip'))
            self.assertEqual(len(archives), 7)
            for archive in archives:
                with zipfile.ZipFile(archive) as bundle:
                    names = set(bundle.namelist())
                    skill = archive.stem
                    self.assertIn(f'{skill}/SKILL.md', names)
                    # The creative review relies on evidence through anti-patterns, even
                    # when prose accidentally stops using a build-recognized path.
                    if skill == 'genz-cringe-check':
                        for resource in ('anti-patterns.md', 'patterns.md', 'claim-ledger.md'):
                            self.assertIn(f'{skill}/references/{resource}', names)
                    self.assertEqual(len(names), len(bundle.namelist()), archive)
                    for name in names:
                        self.assertFalse(name.startswith('/') or '..' in Path(name).parts)
                        content = bundle.read(name).decode('utf-8')
                        for ref in build.REF.findall(content):
                            self.assertIn(f'{skill}/{ref}', names, (name, ref))
                        # Also catches ordinary relative links ignored by build.REF.
                        for link in LOCAL_LINK.findall(content):
                            if '://' not in link:
                                target = str(Path(name).parent / link)
                                self.assertIn(target, names, (name, link))

    def test_chatgpt_flat_files_match_source_and_limits(self):
        with tempfile.TemporaryDirectory() as tmp, patch.object(build, 'DIST', Path(tmp)):
            build.build_chatgpt()
            out = Path(tmp) / 'chatgpt'
            knowledge = list((out / 'knowledge').glob('*.md'))
            expected = sum(1 + len(list((d / 'references').glob('*.md')))
                           for d in build.skill_dirs())
            self.assertEqual(len(knowledge), expected)
            self.assertLessEqual(len(knowledge), build.GPT_KNOWLEDGE_MAX_FILES)
            instructions = build.read(out / 'instructions.md')
            self.assertEqual(instructions, build.read(build.GPT_TEMPLATE))
            self.assertLessEqual(len(instructions), build.GPT_INSTRUCTIONS_MAX)
            for path in knowledge:
                content = build.read(path)
                self.assertFalse(build.REF.findall(content), path)
                for link in LOCAL_LINK.findall(content):
                    if '://' not in link:
                        self.assertTrue((path.parent / link).is_file(), (path, link))

    def test_reference_rewrite_does_not_modify_source(self):
        source = build.SKILLS / 'genz-cringe-check/SKILL.md'
        before = source.read_bytes()
        with tempfile.TemporaryDirectory() as tmp, patch.object(build, 'DIST', Path(tmp)):
            build.build_claude_ai()
            build.build_chatgpt()
        self.assertEqual(source.read_bytes(), before)


if __name__ == '__main__':
    unittest.main()
