#!/usr/bin/env python3
"""List high-star recent AI-ecosystem repos that are missing from docs/.

Usage: requires GITHUB_TOKEN env var or `gh auth token`.
Prints candidates sorted by stars; curate manually into docs/.
"""
import glob
import json
import os
import re
import subprocess
import time
import urllib.parse
import urllib.request

QUERIES = [
    "created:>2026-01-01 stars:>3000 topic:ai",
    "created:>2026-01-01 stars:>3000 ai agent in:description",
    "created:>2025-06-01 stars:>8000 coding agent in:description",
    "created:>2025-06-01 stars:>8000 claude in:description",
    "created:>2025-06-01 stars:>8000 mcp in:description",
]

TOKEN = os.environ.get("GITHUB_TOKEN") or subprocess.run(
    ["gh", "auth", "token"], capture_output=True, text=True).stdout.strip()


def search(q, pages=2):
    items = []
    for p in range(1, pages + 1):
        url = (f"https://api.github.com/search/repositories?"
               f"q={urllib.parse.quote(q)}&sort=stars&order=desc&per_page=100&page={p}")
        req = urllib.request.Request(url, headers={
            "Authorization": f"Bearer {TOKEN}",
            "Accept": "application/vnd.github+json",
            "User-Agent": "we-can-use-discover",
        })
        with urllib.request.urlopen(req) as r:
            items += json.load(r)["items"]
        time.sleep(2.1)
    return items


def main():
    seen = {}
    for q in QUERIES:
        for it in search(q):
            seen[it["full_name"]] = it

    root = os.path.join(os.path.dirname(__file__), "..")
    have = set()
    for f in glob.glob(os.path.join(root, "docs", "*.md")):
        have |= {m.lower() for m in re.findall(r"github\.com/([\w.-]+/[\w.-]+)", open(f).read())}

    missing = sorted((it for k, it in seen.items() if k.lower() not in have),
                     key=lambda it: -it["stargazers_count"])
    for it in missing:
        print(f'{it["stargazers_count"]:>7}  {it["created_at"][:10]}  '
              f'{it["full_name"]:45}  {(it["description"] or "")[:110]}')


if __name__ == "__main__":
    main()
