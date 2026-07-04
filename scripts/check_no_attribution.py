#!/usr/bin/env python3
"""Repo-hygiene gate: fail if any tracked/staged file leaks AI attribution or employer identity.

This is a personal FOSS project authored by Sanjeev Azad. Code, comments, docs, and commit
messages must not (a) advertise an AI author, or (b) reference the author's employer. We ban the
AI vendor words + classic attribution phrases, and the employer names/email. CLAUDE.md and
.claude/ are allowlisted (they legitimately name the local tool and are not published authorship).

Note on "GL": the standalone two-letter token is NOT blanket-banned because "GL" = General Ledger
is a legitimate financial-ontology term (FIBO uses it). We ban the unambiguous employer forms
(GlobalLogic / Global Logic / @globallogic) instead.

Usage:
    python scripts/check_no_attribution.py [files...]   # defaults to `git ls-files`
Exit code 1 on any violation.
"""
import re
import subprocess
import sys

# Allowlisted paths (local tooling config, not published authorship claims).
ALLOW_PREFIXES = (".claude/",)
ALLOW_FILES = {"CLAUDE.md", "scripts/check_no_attribution.py"}

# References to the local tooling files themselves are not attribution — scrub them first.
FILENAME_TOKENS = re.compile(r"(?i)claude\.md|\.claude\b")

BANNED = re.compile(
    r"(?i)\b(claude|anthropic)\b"
    r"|co-authored-by:\s*(claude|anthropic)"
    r"|generated with\s+claude"
    r"|\U0001F916\s*generated"          # 🤖 generated
    r"|\bglobal\s?logic\b"              # employer: GlobalLogic / Global Logic
    r"|@globallogic"                    # work email domain
    r"|\bhitachi\b",                    # parent company
)

# Binary/irrelevant extensions to skip.
SKIP_EXT = (".png", ".jpg", ".jpeg", ".woff", ".woff2", ".ttf", ".ico", ".pdf", ".zip")


def tracked_files():
    out = subprocess.run(["git", "ls-files"], capture_output=True, text=True)
    return [f for f in out.stdout.splitlines() if f]


def is_allowed(path: str) -> bool:
    return path in ALLOW_FILES or path.startswith(ALLOW_PREFIXES)


def main(argv):
    files = argv[1:] or tracked_files()
    violations = []
    for path in files:
        if is_allowed(path) or path.endswith(SKIP_EXT):
            continue
        try:
            with open(path, encoding="utf-8", errors="ignore") as fh:
                for n, line in enumerate(fh, 1):
                    scrubbed = FILENAME_TOKENS.sub("", line)  # ignore CLAUDE.md/.claude filename refs
                    if BANNED.search(scrubbed):
                        violations.append((path, n, line.strip()[:120]))
        except (FileNotFoundError, IsADirectoryError):
            continue

    if violations:
        print("AI-attribution guard FAILED — remove these before committing:")
        for path, n, text in violations:
            print(f"  {path}:{n}: {text}")
        return 1
    print("attribution guard: clean")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
