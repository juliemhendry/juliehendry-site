#!/usr/bin/env python3
"""
Sync beò Lab Notes into writing.html from beo.llc/blog/posts.json

Fetches the posts feed from beo.llc, generates HTML article blocks,
and replaces the content between marker comments in writing.html.

Usage:
    python scripts/sync-writing.py

The script expects:
    - A JSON feed at https://beo.llc/blog/posts.json
    - Marker comments in writing.html:
        <!-- BEO_POSTS_START -->
        ... auto-generated content ...
        <!-- BEO_POSTS_END -->
"""

import json
import sys
import urllib.request
import urllib.error
from html import escape
from pathlib import Path

FEED_URL = "https://beo.llc/blog/posts.json"
WRITING_FILE = Path(__file__).resolve().parent.parent / "writing.html"
START_MARKER = "<!-- BEO_POSTS_START -->"
END_MARKER = "<!-- BEO_POSTS_END -->"


def fetch_posts(url):
    """Fetch and parse the posts JSON feed."""
    req = urllib.request.Request(url, headers={
        "User-Agent": "juliehendry-site-sync/1.0",
        "Accept": "application/json",
    })
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except urllib.error.URLError as e:
        print(f"Error fetching {url}: {e}", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON from {url}: {e}", file=sys.stderr)
        sys.exit(1)

    return data


def generate_html(feed_data):
    """Generate HTML article blocks from the feed data."""
    base_url = feed_data.get("base_url", "https://beo.llc").rstrip("/")
    source = escape(feed_data.get("source", "beò Lab Notes"))
    posts = feed_data.get("posts", [])

    if not posts:
        return "      <!-- No posts found in feed -->\n"

    blocks = []
    for post in posts:
        title = escape(post["title"])
        date = escape(post["date"])
        excerpt = escape(post.get("excerpt", ""))
        path = post["path"]
        url = f"{base_url}{path}" if path.startswith("/") else path

        block = f"""      <article class="work-block">
        <div class="era-label">{source} &middot; {date}</div>
        <h3>{title}</h3>
        <p>{excerpt}</p>
        <a href="{escape(url)}" class="work-link">Read the full post at beò</a>
      </article>"""
        blocks.append(block)

    return "\n\n".join(blocks) + "\n"


def update_writing_html(new_content, post_count):
    """Replace content between markers in writing.html. Returns True if changed."""
    html = WRITING_FILE.read_text(encoding="utf-8")

    start_idx = html.find(START_MARKER)
    end_idx = html.find(END_MARKER)

    if start_idx == -1 or end_idx == -1:
        print(f"Error: markers not found in {WRITING_FILE}", file=sys.stderr)
        print(f"  Expected: {START_MARKER}", file=sys.stderr)
        print(f"  Expected: {END_MARKER}", file=sys.stderr)
        sys.exit(1)

    if end_idx <= start_idx:
        print("Error: END marker appears before START marker", file=sys.stderr)
        sys.exit(1)

    before = html[:start_idx + len(START_MARKER)]
    after = html[end_idx:]

    updated = before + "\n" + new_content + "      " + after

    # Only write if content actually changed
    if updated == html:
        print("No changes detected, writing.html is up to date.")
        return False

    WRITING_FILE.write_text(updated, encoding="utf-8")
    print(f"Updated {WRITING_FILE} with {post_count} posts.")
    return True


if __name__ == "__main__":
    print(f"Fetching posts from {FEED_URL}...")
    feed_data = fetch_posts(FEED_URL)

    posts = feed_data.get("posts", [])
    print(f"Found {len(posts)} posts.")

    html_content = generate_html(feed_data)
    update_writing_html(html_content, len(posts))
