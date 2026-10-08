#!/usr/bin/env python3
"""One-off import of the Google Sites pages of www.awallet.org into Markdown (migration step 2).

Usage: .venv/bin/python tools/import_google_sites.py <dir-with-crawled-html>

Keeps what the old site promised to links from apps, stores and search engines:
- every heading gets its original Google Sites anchor as an explicit id (`## Title {#h.xxxx}`), the
  target of links like /faq#h.2a86ld1hnga3 (the empty <div id="h.xxxx"> Sites puts before each heading);
- internal links become relative Markdown links (the preview lives under /awallet-website/);
- images are downloaded into docs/assets/<page>/.
The Sites table-of-contents block is dropped (Material renders its own), as is the Sites chrome.
Output is a starting point: pages are reviewed and tidied by hand afterwards.
"""
import html, os, re, sys, urllib.parse, urllib.request
from bs4 import BeautifulSoup, NavigableString
from markdownify import MarkdownConverter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(ROOT, "docs")
SITE = "https://www.awallet.org"

# crawled file stem -> (site path, markdown file)
PAGES = {
    "home": ("/", "index.md"),
    "home_feature-matrix": ("/home/feature-matrix", "home/feature-matrix.md"),
    "download": ("/download", "download.md"),
    "faq": ("/faq", "faq.md"),
    "faq-cloud": ("/faq-cloud", "faq-cloud/index.md"),
    "faq-cloud_restore-google-drive-revision": ("/faq-cloud/restore-google-drive-revision",
                                                "faq-cloud/restore-google-drive-revision.md"),
    "faq-ios": ("/faq-ios", "faq-ios.md"),
    "documentation": ("/documentation", "documentation/index.md"),
    "documentation_privacy-policy": ("/documentation/privacy-policy", "documentation/privacy-policy.md"),
    "documentation_technical-documentation": ("/documentation/technical-documentation",
                                              "documentation/technical-documentation.md"),
    "contact": ("/contact", "contact.md"),
}
PATH_TO_MD = {p: md for p, md in PAGES.values()}
PATH_TO_MD["/home"] = "index.md"


def unwrap_google(href):
    """Google Sites wraps outbound links in https://www.google.com/url?q=<target>&…"""
    if href and re.match(r"https?://www\.google\.com/url\?", href):
        q = urllib.parse.parse_qs(urllib.parse.urlparse(href).query).get("q")
        if q:
            return q[0]
    return href


def rel_link(href, from_md):
    """Internal awallet.org link -> relative link to the Markdown page (MkDocs resolves it)."""
    href = unwrap_google(href)
    u = urllib.parse.urlparse(href)
    if u.netloc in ("www.awallet.org", "awallet.org") or (not u.netloc and href.startswith("/")):
        path = u.path.rstrip("/") or "/"
        md = PATH_TO_MD.get(path)
        if md:
            rel = os.path.relpath(md, os.path.dirname(from_md) or ".")
            return rel + (("#" + u.fragment) if u.fragment else "")
    if not u.netloc and href.startswith("#"):
        return href
    return href


class Conv(MarkdownConverter):
    def __init__(self, from_md, **kw):
        super().__init__(heading_style="ATX", bullets="-", **kw)
        self.from_md = from_md

    def convert_a(self, el, text, *args, **kw):
        href = el.get("href")
        if not href:
            return text
        el["href"] = rel_link(html.unescape(href), self.from_md)
        return super().convert_a(el, text, *args, **kw)

    def _heading(self, el, text, level):
        text = " ".join(text.split())
        if not text:
            return ""
        anchor = el.get("data-anchor")
        if not anchor:
            return "\n\n" + "#" * level + " " + text + "\n\n"
        # Sites answers both #h.xxxx and #h.xxxx_l (the apps link the privacy policy's EULA by the _l form)
        return f'\n\n<a id="{anchor}_l"></a>\n\n' + "#" * level + " " + text + " {#" + anchor + "}\n\n"

    def convert_h1(self, el, text, *a, **k): return self._heading(el, text, 1)
    def convert_h2(self, el, text, *a, **k): return self._heading(el, text, 2)
    def convert_h3(self, el, text, *a, **k): return self._heading(el, text, 3)
    def convert_h4(self, el, text, *a, **k): return self._heading(el, text, 4)


def download_image(src, page_stem, n):
    folder = os.path.join(DOCS, "assets", page_stem)
    os.makedirs(folder, exist_ok=True)
    req = urllib.request.Request(src, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        data = r.read()
        ctype = r.headers.get("Content-Type", "")
    ext = ".jpg" if "jpeg" in ctype else ".gif" if "gif" in ctype else ".webp" if "webp" in ctype else ".png"
    name = f"img-{n:02d}{ext}"
    with open(os.path.join(folder, name), "wb") as f:
        f.write(data)
    return f"assets/{page_stem}/{name}"


def import_page(stem, html_path):
    site_path, md_file = PAGES[stem]
    soup = BeautifulSoup(open(html_path, encoding="utf-8").read(), "html.parser")
    out = soup.new_tag("div")
    img_n = 0
    sections = [s for s in soup.find_all("section") if s.find_parent("header") is None]
    for sec in sections:
        for el in sec.find_all(["div", "img", "iframe"]):
            classes = el.get("class") or []
            if el.name == "div" and "tyJCtd" in classes:
                if el.select_one(".pBmh1[data-id]"):          # Sites table of contents
                    continue
                block = BeautifulSoup(str(el), "html.parser")
                for marker in block.select("div.CobnVe[id]"):  # anchor target before each heading
                    h = marker.find_next(["h1", "h2", "h3", "h4"])
                    if h is not None:
                        h["data-anchor"] = marker["id"]
                for tag in block.find_all(["h1", "h2", "h3", "h4"]):
                    if not tag.get("data-anchor") and (tag.get("id") or "").endswith("_l"):
                        tag["data-anchor"] = tag["id"][:-2]
                for img in block.find_all("img"):            # images live inside the blocks (store badges in links)
                    src = img.get("src") or ""
                    if not src.startswith("http"):
                        continue
                    img_n += 1
                    try:
                        local = download_image(src, stem, img_n)
                    except Exception as e:
                        print(f"  image {img_n} of {stem} failed: {e}")
                        continue
                    img["src"] = os.path.relpath(local, os.path.dirname(md_file) or ".")
                    img["alt"] = img.get("alt") or ""
                out.append(block)
            elif el.name == "div" and el.has_attr("data-code"):   # Sites "Embed code" block: hand-made HTML tables
                embed = BeautifulSoup(el["data-code"], "html.parser")
                for table in embed.find_all("table"):           # first row is the header -> Markdown table
                    first = table.find("tr")
                    if first is not None:
                        for td in first.find_all("td"):
                            td.name = "th"
                for tag in embed.find_all(True):
                    for attr in ("style", "width", "height", "border", "bordercolor", "cellspacing"):
                        tag.attrs.pop(attr, None)
                out.append(embed)
            elif el.name == "iframe" and not el.find_parent(attrs={"data-code": True}):
                src = el.get("src") or el.get("data-src") or ""
                p = soup.new_tag("p")
                if "youtube.com/embed/" in src:
                    vid = src.split("youtube.com/embed/")[1].split("?")[0]
                    p.append(NavigableString(f"VIDEO:{vid}"))
                else:
                    p.append(NavigableString(f"TODO-EMBED: {src[:80]}"))
                out.append(p)
    md = Conv(md_file).convert_soup(out)
    md = re.sub(r"VIDEO:([\w-]+)", lambda m: f'<iframe width="560" height="315" src="https://www.youtube.com/embed/{m.group(1)}" '
                                              f'title="YouTube video" frameborder="0" allowfullscreen></iframe>', md)
    md = re.sub(r"(?m)^[ \t\u00a0]+$", "", md)                 # spacer paragraphs (&nbsp;) of the Sites layout
    md = re.sub(r"(?m)[ \t]+$", "", md)
    md = re.sub(r"\n{3,}", "\n\n", md).strip() + "\n"
    target = os.path.join(DOCS, md_file)
    os.makedirs(os.path.dirname(target), exist_ok=True)
    open(target, "w", encoding="utf-8").write(md)
    anchors = len(re.findall(r"\{#h\.", md))
    print(f"{site_path:45} -> docs/{md_file:45} {len(md.split()):5} words, {anchors:3} anchors, {img_n} images")


if __name__ == "__main__":
    src_dir = sys.argv[1]
    for stem in PAGES:
        import_page(stem, os.path.join(src_dir, stem + ".html"))
