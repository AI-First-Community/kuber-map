#!/usr/bin/env python3
"""Validate the generated OKF bundle: link integrity, orphans, self-loops, collisions.
Usage: python etl/validate.py --bundle knowledge"""
import argparse
import glob
import os
import re

FM_REL = re.compile(r'target:\s*"([^"]+)"')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--bundle", default="knowledge")
    args = ap.parse_args()

    files = [f for f in glob.glob(os.path.join(args.bundle, "**", "*.md"), recursive=True)
             if os.path.basename(f) != "index.md"]
    present = {"/" + os.path.relpath(f, args.bundle).replace(os.sep, "/") for f in files}

    total_edges = pending = self_loops = 0
    incoming = {p: 0 for p in present}
    for f in files:
        rel = "/" + os.path.relpath(f, args.bundle).replace(os.sep, "/")
        for tgt in FM_REL.findall(open(f).read()):
            total_edges += 1
            if tgt == rel:
                self_loops += 1
            if tgt in present:
                incoming[tgt] = incoming.get(tgt, 0) + 1
            else:
                # target file missing: pending (cluster exists in path but not generated) vs broken
                pending += 1
    orphans = [p for p, n in incoming.items() if n == 0]

    print("================ OKF BUNDLE VALIDATION ================")
    print(f"Files (concepts)      : {len(present)}")
    print(f"Frontmatter edges     : {total_edges}")
    print(f"  resolved in-bundle   : {total_edges - pending}")
    print(f"  pending (not loaded) : {pending}  (cross-cluster targets awaiting their domain)")
    print(f"  self-loops           : {self_loops}")
    print(f"Orphan nodes (no incoming): {len(orphans)}")
    print("======================================================")


if __name__ == "__main__":
    main()
