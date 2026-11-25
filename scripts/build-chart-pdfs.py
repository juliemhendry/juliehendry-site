#!/usr/bin/env python3
"""Rebuild the two CHART PDFs from source.

CHART/CHART-framework.pdf is printed from CHART/framework.html (the web page is the source).
CHART/five-questions.pdf is printed from scripts/pdf/five-questions.html.
Needs Google Chrome (headless) and pikepdf. Run from the repo root:
    python3 scripts/build-chart-pdfs.py
"""
import re, subprocess, pathlib, shutil, tempfile, pikepdf

ROOT = pathlib.Path(__file__).resolve().parent.parent
PDFDIR = ROOT / "scripts" / "pdf"
CHROME = shutil.which("google-chrome") or shutil.which("chromium") or "google-chrome"


def framework_print_html() -> str:
    src = (ROOT / "CHART" / "framework.html").read_text(encoding="utf-8")
    main = re.search(r'<main id="content">(.*?)</main>', src, re.S).group(1)
    main = re.sub(r'<a href="/CHART/CHART-framework.pdf">Download as PDF</a> &middot; ', "", main)
    main = main.replace('class="btn"', "")
    main = main.replace('href="/', 'href="https://juliehendry.com/')
    return f"""<!DOCTYPE html><html lang="en-GB"><head><meta charset="UTF-8">
<title>CHART: Cognitive Health Assessment for Responsible Technology</title>
<link rel="stylesheet" href="print.css">
<style>@page{{@bottom-left{{content:"CHART · juliehendry.com";font:8pt Inter,sans-serif;color:#777}}}}
.label{{color:#555}} header h1{{font-size:20pt}}</style></head><body>{main}</body></html>"""


def print_pdf(html_path: pathlib.Path, out: pathlib.Path, title: str):
    subprocess.run([CHROME, "--headless", "--disable-gpu", "--no-sandbox", "--no-pdf-header-footer",
                    f"--print-to-pdf={out}", html_path.as_uri()], check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    with pikepdf.open(out, allow_overwriting_input=True) as pdf:
        with pdf.open_metadata() as meta:
            meta["dc:title"] = title
            meta["dc:creator"] = ["Julie Hendry"]
        pdf.docinfo["/Title"] = title
        pdf.docinfo["/Author"] = "Julie Hendry"
        pdf.save(out)


if __name__ == "__main__":
    tmp = PDFDIR / "_framework.print.html"
    tmp.write_text(framework_print_html(), encoding="utf-8")
    try:
        print_pdf(tmp, ROOT / "CHART" / "CHART-framework.pdf",
                  "CHART: Cognitive Health Assessment for Responsible Technology")
    finally:
        tmp.unlink(missing_ok=True)
    print_pdf(PDFDIR / "five-questions.html", ROOT / "CHART" / "five-questions.pdf",
              "Five Questions Your Board Should Be Asking About AI Oversight")
    print("Built CHART/CHART-framework.pdf and CHART/five-questions.pdf")
