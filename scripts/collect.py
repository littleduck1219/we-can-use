#!/usr/bin/env python3
"""Generate the full catalogs (catalog/*.md) from GitHub topic search.

Usage: requires the GITHUB_TOKEN env var or `gh auth token`.
The Search API caps each query at 1000 results, so we split star ranges.
"""
import html
import json
import math
import os
import subprocess
import time
import urllib.request


API = "https://api.github.com/search/repositories"
MIN_STARS = 10
MAX_STARS = 1_000_000
ROWS_PER_FILE = 1000

# Catalog definitions: (file slug, title, topic list)
CATALOGS = [
    ("mcp-servers", "Full MCP Server Catalog", ["mcp-server", "mcp-servers"]),
    ("skills-plugins", "Full Skills & Plugins Catalog",
     ["claude-code", "claude-code-plugin", "claude-code-plugins", "claude-code-subagents",
      "claude-skills", "claude-skill", "agent-skills", "agent-skill"]),
]


def token() -> str:
    t = os.environ.get("GITHUB_TOKEN")
    if not t:
        t = subprocess.run(["gh", "auth", "token"], capture_output=True, text=True).stdout.strip()
    if not t:
        raise SystemExit("GITHUB_TOKEN is missing")
    return t


TOKEN = token()


def search(q: str, page: int = 1):
    url = f"{API}?q={urllib.parse.quote(q)}&sort=stars&order=desc&per_page=100&page={page}"
    req = urllib.request.Request(url, headers={
        "Authorization": f"Bearer {TOKEN}",
        "Accept": "application/vnd.github+json",
        "User-Agent": "we-can-use-catalog",
    })
    for attempt in range(5):
        try:
            with urllib.request.urlopen(req) as r:
                data = json.load(r)
            time.sleep(2.1)  # authenticated search limit: 30 req/min
            return data
        except urllib.error.HTTPError as e:
            if e.code in (403, 429):  # rate limit -> wait and retry
                time.sleep(30 * (attempt + 1))
                continue
            raise
    raise SystemExit(f"search failed: {q}")


def fetch_topic(topic: str) -> dict:
    """Collect everything by bisecting star ranges to bypass the 1000-result cap."""
    repos = {}
    stack = [(MIN_STARS, MAX_STARS)]
    while stack:
        lo, hi = stack.pop()
        q = f"topic:{topic} stars:{lo}..{hi} archived:false"
        first = search(q)
        total = first["total_count"]
        if total > 1000 and lo < hi:
            mid = (lo + hi) // 2
            stack.append((lo, mid))
            stack.append((mid + 1, hi))
            continue
        if total > 1000:  # >1000 repos at one star count (practically never)
            print(f"  warning: {q} -> {total} repos, collecting top 1000 only")
        pages = min(10, math.ceil(min(total, 1000) / 100))
        for item in first["items"]:
            repos[item["full_name"]] = item
        for p in range(2, pages + 1):
            for item in search(q, p)["items"]:
                repos[item["full_name"]] = item
        print(f"  {q} -> {total} repos")
    return repos


def write_catalog(slug: str, title: str, repos: list):
    os.makedirs("catalog", exist_ok=True)
    n_files = max(1, math.ceil(len(repos) / ROWS_PER_FILE))
    for i in range(n_files):
        chunk = repos[i * ROWS_PER_FILE:(i + 1) * ROWS_PER_FILE]
        path = f"catalog/{slug}.md" if i == 0 else f"catalog/{slug}-{i + 1}.md"
        nav = " · ".join(
            f"[{j + 1}]({slug}.md)" if j == 0 else f"[{j + 1}]({slug}-{j + 1}.md)"
            for j in range(n_files)
        )
        with open(path, "w") as f:
            f.write(f"# {title}\n\n")
            if n_files > 1:
                f.write(f"Pages: {nav}\n\n")
            f.write('<table width="100%">\n')
            f.write('<tr><th width="340">Repository</th><th width="90">Stars</th><th>Description</th></tr>\n')
            for r in chunk:
                desc = html.escape(r["description"] or "").strip()
                f.write(f'<tr><td><a href="{r["html_url"]}">{html.escape(r["full_name"])}</a></td>'
                        f'<td>⭐ {r["stargazers_count"]:,}</td><td>{desc}</td></tr>\n')
            f.write("</table>\n")
    print(f"{slug}: {len(repos)} repos -> {n_files} files")


def main():
    for slug, title, topics in CATALOGS:
        print(f"[{slug}]")
        merged = {}
        for t in topics:
            merged.update(fetch_topic(t))
        repos = sorted(merged.values(), key=lambda r: -r["stargazers_count"])
        write_catalog(slug, title, repos)


if __name__ == "__main__":
    import urllib.parse  # noqa: E402
    main()
