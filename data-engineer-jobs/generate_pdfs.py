#!/usr/bin/env python3
"""Generate ATS-friendly PDF resumes from markdown files."""

from pathlib import Path
import re

from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import HRFlowable, Paragraph, SimpleDocTemplate, Spacer

RESUMES_DIR = Path(__file__).parent / "resumes"
PDFS_DIR = Path(__file__).parent / "pdfs"


def parse_markdown(content: str) -> list[tuple[str, str]]:
    """Parse markdown resume into (type, text) blocks."""
    blocks: list[tuple[str, str]] = []
    lines = content.strip().split("\n")
    i = 0

    # Header block before first ---
    header_lines = []
    while i < len(lines) and not lines[i].strip().startswith("---"):
        if lines[i].startswith("# "):
            header_lines.append(("name", lines[i][2:].strip()))
        elif lines[i].strip():
            header_lines.append(("contact", lines[i].strip()))
        i += 1
    for block_type, text in header_lines:
        blocks.append((block_type, text))

    if i < len(lines) and lines[i].strip() == "---":
        i += 1

    current_section = ""
    current_body: list[str] = []

    def flush_section():
        nonlocal current_section, current_body
        if current_section:
            body = "\n".join(current_body).strip()
            if body:
                blocks.append(("section", current_section))
                blocks.append(("body", body))
        current_section = ""
        current_body = []

    while i < len(lines):
        line = lines[i]
        if line.strip() == "---":
            flush_section()
            i += 1
            continue
        if line.startswith("## "):
            flush_section()
            current_section = line[3:].strip()
            i += 1
            continue
        if line.startswith("### "):
            if current_body:
                current_body.append("")
            current_body.append(line[4:].strip())
            i += 1
            continue
        if line.startswith("- "):
            current_body.append("• " + line[2:].strip())
            i += 1
            continue
        if line.strip():
            current_body.append(line.strip())
        i += 1

    flush_section()
    return blocks


def clean_inline(text: str) -> str:
    """Convert markdown inline formatting to reportlab-safe XML."""
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    text = text.replace("&", "&amp;").replace("<b>", "§B§").replace("</b>", "§/B§")
    text = text.replace("<", "&lt;").replace(">", "&gt;")
    text = text.replace("§B§", "<b>").replace("§/B§", "</b>")
    return text


def build_pdf(blocks: list[tuple[str, str]], output_path: Path) -> None:
    doc = SimpleDocTemplate(
        str(output_path),
        pagesize=letter,
        leftMargin=0.65 * inch,
        rightMargin=0.65 * inch,
        topMargin=0.55 * inch,
        bottomMargin=0.55 * inch,
    )

    styles = getSampleStyleSheet()
    name_style = ParagraphStyle(
        "Name",
        parent=styles["Heading1"],
        fontName="Helvetica-Bold",
        fontSize=16,
        leading=20,
        spaceAfter=4,
        alignment=TA_LEFT,
    )
    contact_style = ParagraphStyle(
        "Contact",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=9,
        leading=12,
        spaceAfter=2,
        alignment=TA_LEFT,
    )
    section_style = ParagraphStyle(
        "Section",
        parent=styles["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=11,
        leading=14,
        spaceBefore=8,
        spaceAfter=4,
        alignment=TA_LEFT,
    )
    body_style = ParagraphStyle(
        "Body",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=9.5,
        leading=13,
        spaceAfter=3,
        alignment=TA_LEFT,
    )
    bullet_style = ParagraphStyle(
        "Bullet",
        parent=body_style,
        leftIndent=12,
        bulletIndent=0,
        spaceAfter=2,
    )

    story = []

    for block_type, text in blocks:
        text = clean_inline(text)
        if block_type == "name":
            story.append(Paragraph(text, name_style))
        elif block_type == "contact":
            story.append(Paragraph(text, contact_style))
        elif block_type == "section":
            story.append(Spacer(1, 4))
            story.append(HRFlowable(width="100%", thickness=0.5, color="#333333"))
            story.append(Paragraph(text.upper(), section_style))
        elif block_type == "body":
            for line in text.split("\n"):
                if not line.strip():
                    story.append(Spacer(1, 4))
                elif line.startswith("• "):
                    story.append(Paragraph(line, bullet_style))
                else:
                    story.append(Paragraph(line, body_style))

    doc.build(story)


def main() -> None:
    PDFS_DIR.mkdir(parents=True, exist_ok=True)
    generated = []

    for md_file in sorted(RESUMES_DIR.glob("*-resume.md")):
        content = md_file.read_text(encoding="utf-8")
        blocks = parse_markdown(content)
        pdf_name = md_file.stem + ".pdf"
        pdf_path = PDFS_DIR / pdf_name
        build_pdf(blocks, pdf_path)
        generated.append(pdf_path.name)
        print(f"Generated: {pdf_path}")

    print(f"\nTotal PDFs generated: {len(generated)}")


if __name__ == "__main__":
    main()
