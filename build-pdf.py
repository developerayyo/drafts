#!/usr/bin/env python3
"""Build PDFs for McGrocer ops-pack — flow (mermaid), briefs, rescore."""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent
BUILD = ROOT / ".build"

FLOW_MD = ROOT / "mcgrocer-2.0-automated-operations-flow.md"
FLOW_PDF = ROOT / "mcgrocer-2.0-automated-operations-flow.pdf"

EXTRA_DOCS = [
    (ROOT / "mike-review-brief.md", ROOT / "mike-review-brief.pdf", "McGrocer — Mike Review Brief"),
    (
        ROOT / "aisha-delta-brief-v3.8.2.md",
        ROOT / "aisha-delta-brief-v3.8.2.pdf",
        "McGrocer — Aisha Delta Brief",
    ),
    (
        ROOT / "McGrocer_V2_stress_test_Plan_v3.8.2_rescore.md",
        ROOT / "McGrocer_V2_stress_test_Plan_v3.8.2_rescore.pdf",
        "McGrocer V2 — Gap Re-score v3.8.3",
    ),
]

MERMAID_RE = re.compile(r"```mermaid\n(.*?)```", re.DOTALL)

CSS = """
@page {
  size: A4;
  margin: 18mm 16mm 20mm 16mm;
  @bottom-center {
    content: counter(page);
    font-size: 9pt;
    color: #666;
  }
}

* { box-sizing: border-box; }

body {
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-size: 10.5pt;
  line-height: 1.45;
  color: #111;
  max-width: 100%;
}

h1 {
  font-size: 20pt;
  margin: 0 0 12pt;
  page-break-after: avoid;
  border-bottom: 2px solid #222;
  padding-bottom: 6pt;
}

h2 {
  font-size: 14pt;
  margin: 18pt 0 8pt;
  page-break-after: avoid;
  border-bottom: 1px solid #ccc;
  padding-bottom: 4pt;
}

h3 {
  font-size: 11.5pt;
  margin: 14pt 0 6pt;
  page-break-after: avoid;
}

h4, h5, h6 {
  font-size: 10.5pt;
  margin: 10pt 0 4pt;
  page-break-after: avoid;
}

p, li { margin: 0 0 6pt; }

ul, ol { margin: 0 0 8pt 18pt; padding: 0; }

blockquote {
  margin: 8pt 0;
  padding: 8pt 12pt;
  border-left: 3px solid #888;
  background: #f7f7f7;
  color: #222;
}

blockquote p { margin: 0 0 4pt; }
blockquote p:last-child { margin-bottom: 0; }

hr {
  border: none;
  border-top: 1px solid #ccc;
  margin: 14pt 0;
}

table {
  width: 100%;
  border-collapse: collapse;
  margin: 8pt 0 12pt;
  font-size: 9.5pt;
  page-break-inside: auto;
}

thead { display: table-header-group; }
tr { page-break-inside: avoid; }

th, td {
  border: 1px solid #bbb;
  padding: 5pt 6pt;
  text-align: left;
  vertical-align: top;
}

th {
  background: #efefef;
  font-weight: 600;
}

code {
  font-family: "DejaVu Sans Mono", "Liberation Mono", monospace;
  font-size: 9pt;
  background: #f3f3f3;
  padding: 1pt 3pt;
  border-radius: 2px;
}

pre {
  font-family: "DejaVu Sans Mono", "Liberation Mono", monospace;
  font-size: 8.5pt;
  line-height: 1.35;
  background: #f5f5f5;
  border: 1px solid #ddd;
  padding: 8pt;
  overflow-x: auto;
  white-space: pre-wrap;
  word-wrap: break-word;
  page-break-inside: avoid;
}

pre code { background: none; padding: 0; }

.diagram {
  margin: 10pt 0 14pt;
  page-break-inside: avoid;
  text-align: center;
}

.diagram img {
  max-width: 100%;
  height: auto;
  border: 1px solid #ddd;
}

.diagram-fallback {
  margin: 10pt 0 14pt;
  page-break-inside: avoid;
}

.diagram-fallback .caption {
  font-size: 9pt;
  color: #555;
  margin-bottom: 4pt;
}

a { color: #111; text-decoration: none; }

strong { font-weight: 600; }
"""


def run(cmd: list[str], **kwargs) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, check=True, text=True, capture_output=True, **kwargs)


def render_mermaid(source: str, index: int, build_dir: Path) -> Path | None:
    diagram_dir = build_dir / "diagrams"
    diagram_dir.mkdir(parents=True, exist_ok=True)
    mmd = diagram_dir / f"diagram-{index:02d}.mmd"
    svg = diagram_dir / f"diagram-{index:02d}.svg"
    puppeteer_cfg = build_dir / "puppeteer-config.json"
    if not puppeteer_cfg.exists():
        puppeteer_cfg.write_text(
            '{"args":["--no-sandbox","--disable-setuid-sandbox","--disable-dev-shm-usage"]}\n',
            encoding="utf-8",
        )
    mmd.write_text(source.strip() + "\n", encoding="utf-8")

    npx = shutil.which("npx") or "npx"
    cmd = [
        npx,
        "-y",
        "@mermaid-js/mermaid-cli",
        "-i",
        str(mmd),
        "-o",
        str(svg),
        "-b",
        "white",
        "-p",
        str(puppeteer_cfg),
        "--width",
        "1400",
        "--scale",
        "1",
    ]
    try:
        result = subprocess.run(cmd, text=True, capture_output=True, timeout=180)
        if result.returncode != 0 or not svg.exists():
            print(f"  diagram {index}: mmdc failed\n{result.stderr[:500]}", file=sys.stderr)
            return None
        return svg
    except subprocess.TimeoutExpired:
        print(f"  diagram {index}: timed out", file=sys.stderr)
        return None


def md_to_html(text: str) -> str:
    if not text.strip():
        return ""
    return markdown.markdown(
        text,
        extensions=["tables", "fenced_code", "sane_lists", "nl2br"],
        output_format="html5",
    )


def build_flow_body(md: str, build_dir: Path) -> str:
    parts: list[str] = []
    last = 0
    diagram_index = 0
    total = len(MERMAID_RE.findall(md))

    for match in MERMAID_RE.finditer(md):
        parts.append(md_to_html(md[last : match.start()]))
        source = match.group(1)
        svg = render_mermaid(source, diagram_index, build_dir)
        if svg:
            rel = svg.relative_to(build_dir)
            parts.append(
                f'<div class="diagram"><img src="{rel.as_posix()}" '
                f'alt="Flowchart {diagram_index + 1}"/></div>'
            )
        else:
            escaped = (
                source.replace("&", "&amp;")
                .replace("<", "&lt;")
                .replace(">", "&gt;")
            )
            parts.append(
                f'<div class="diagram-fallback">'
                f'<div class="caption">Flowchart {diagram_index + 1} (source — render failed)</div>'
                f"<pre><code>{escaped}</code></pre></div>"
            )
        diagram_index += 1
        last = match.end()
        print(f"  rendered diagram {diagram_index}/{total}...", flush=True)

    parts.append(md_to_html(md[last:]))
    return "\n".join(parts)


def write_html(body: str, html_file: Path, title: str) -> None:
    html_file.parent.mkdir(parents=True, exist_ok=True)
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8"/>
  <title>{title}</title>
  <style>{CSS}</style>
</head>
<body>
{body}
</body>
</html>
"""
    html_file.write_text(html, encoding="utf-8")


def html_to_pdf(html_file: Path, pdf_file: Path) -> None:
    chrome = shutil.which("google-chrome") or shutil.which("chromium") or shutil.which("chromium-browser")
    if chrome:
        run(
            [
                chrome,
                "--headless=new",
                "--disable-gpu",
                "--no-sandbox",
                "--disable-setuid-sandbox",
                f"--print-to-pdf={pdf_file.resolve()}",
                "--print-to-pdf-no-header",
                f"file://{html_file.resolve()}",
            ],
            timeout=300,
        )
        return

    weasyprint = shutil.which("weasyprint")
    if weasyprint:
        run([weasyprint, str(html_file), str(pdf_file)], timeout=300)
        return

    raise RuntimeError("No PDF engine found (google-chrome or weasyprint)")


def build_flow() -> Path:
    if not FLOW_MD.exists():
        raise SystemExit(f"Missing {FLOW_MD}")

    flow_build = BUILD / "flow"
    flow_html = flow_build / "flow.html"

    print(f"Reading {FLOW_MD.name}...")
    md = FLOW_MD.read_text(encoding="utf-8")
    print(f"  {len(md.splitlines())} lines, {len(MERMAID_RE.findall(md))} mermaid blocks")

    if flow_build.exists():
        shutil.rmtree(flow_build)
    flow_build.mkdir(parents=True)

    print("Building flow HTML...")
    body = build_flow_body(md, flow_build)
    write_html(body, flow_html, "McGrocer 2.0 — Automated Operations Flow")

    print("Generating flow PDF...")
    html_to_pdf(flow_html, FLOW_PDF)
    print(f"Done: {FLOW_PDF} ({FLOW_PDF.stat().st_size // 1024} KB)")
    return FLOW_PDF


def build_simple(md_path: Path, pdf_path: Path, title: str) -> Path:
    if not md_path.exists():
        raise SystemExit(f"Missing {md_path}")

    doc_build = BUILD / md_path.stem
    html_path = doc_build / f"{md_path.stem}.html"

    print(f"Reading {md_path.name}...")
    md = md_path.read_text(encoding="utf-8")
    if doc_build.exists():
        shutil.rmtree(doc_build)
    doc_build.mkdir(parents=True)

    body = md_to_html(md)
    write_html(body, html_path, title)
    html_to_pdf(html_path, pdf_path)
    print(f"Done: {pdf_path} ({pdf_path.stat().st_size // 1024} KB)")
    return pdf_path


def main() -> None:
    parser = argparse.ArgumentParser(description="Build McGrocer ops-pack PDFs")
    parser.add_argument(
        "target",
        nargs="?",
        choices=("flow", "briefs", "all"),
        default="all",
        help="Which PDFs to build (default: all)",
    )
    args = parser.parse_args()

    if args.target in ("flow", "all"):
        build_flow()
    if args.target in ("briefs", "all"):
        for md_path, pdf_path, title in EXTRA_DOCS:
            build_simple(md_path, pdf_path, title)


if __name__ == "__main__":
    main()
