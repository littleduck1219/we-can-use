#!/usr/bin/env python3
"""GitHub 토픽 검색으로 전체 카탈로그(catalog/*.md)를 생성한다.

사용: GITHUB_TOKEN 환경변수 또는 `gh auth token` 필요.
Search API는 쿼리당 1000개 제한이 있어 스타 구간을 쪼개서 수집한다.
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

# 카탈로그 정의: (파일 슬러그, 제목, 토픽 목록)
CATALOGS = [
    ("mcp-servers", "MCP 서버 전체 카탈로그", ["mcp-server", "mcp-servers"]),
    ("skills-plugins", "스킬·플러그인 전체 카탈로그",
     ["claude-code", "claude-code-plugin", "claude-code-plugins", "claude-code-subagents",
      "claude-skills", "claude-skill", "agent-skills", "agent-skill"]),
]


def token() -> str:
    t = os.environ.get("GITHUB_TOKEN")
    if not t:
        t = subprocess.run(["gh", "auth", "token"], capture_output=True, text=True).stdout.strip()
    if not t:
        raise SystemExit("GITHUB_TOKEN이 없습니다")
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
            time.sleep(2.1)  # 인증 검색 한도 30req/min
            return data
        except urllib.error.HTTPError as e:
            if e.code in (403, 429):  # rate limit → 대기 후 재시도
                time.sleep(30 * (attempt + 1))
                continue
            raise
    raise SystemExit(f"검색 실패: {q}")


def fetch_topic(topic: str) -> dict:
    """스타 구간을 이분할하며 1000개 제한을 우회해 전부 수집."""
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
        if total > 1000:  # 같은 스타 수에 1000개 초과 (사실상 없음)
            print(f"  경고: {q} → {total}개, 상위 1000개만 수집")
        pages = min(10, math.ceil(min(total, 1000) / 100))
        for item in first["items"]:
            repos[item["full_name"]] = item
        for p in range(2, pages + 1):
            for item in search(q, p)["items"]:
                repos[item["full_name"]] = item
        print(f"  {q} → {total}개")
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
                f.write(f"페이지: {nav}\n\n")
            f.write('<table width="100%">\n')
            f.write('<tr><th width="340">저장소</th><th width="90">스타</th><th>설명</th></tr>\n')
            for r in chunk:
                desc = html.escape(r["description"] or "").strip()
                f.write(f'<tr><td><a href="{r["html_url"]}">{html.escape(r["full_name"])}</a></td>'
                        f'<td>⭐ {r["stargazers_count"]:,}</td><td>{desc}</td></tr>\n')
            f.write("</table>\n")
    print(f"{slug}: {len(repos)}개 → {n_files}개 파일")


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
