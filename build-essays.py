from pathlib import Path
from datetime import datetime

TEMPLATE_FILE = Path("essay-template.html")
INDEX_TEMPLATE_FILE = Path("essays-template.html")
SOURCE_DIR = Path("essays-source")
OUTPUT_DIR = Path("essays")
INDEX_FILE = Path("essays.html")

TITLE_PLACEHOLDER = "<!-- BUILD-ESSAYS:TITLE -->"
CONTENT_PLACEHOLDER = "<!-- BUILD-ESSAYS:CONTENT -->"
INDEX_PLACEHOLDER = "<!-- BUILD-ESSAYS:INDEX -->"


def read_essay(source_file):
    lines = source_file.read_text(encoding="utf-8").splitlines()

    if not lines or lines[0].strip() != "<!--":
        raise ValueError(f"{source_file}: Missing metadata block.")

    metadata = {}
    body_start = None

    for i in range(1, len(lines)):
        line = lines[i]

        if line.strip() == "-->":
            body_start = i + 1
            break

        if ":" in line:
            key, value = line.split(":", 1)
            metadata[key.strip()] = value.strip()

    if body_start is None:
        raise ValueError(f"{source_file}: Metadata block not closed.")

    required = ("Title", "Date")
    for key in required:
        if key not in metadata:
            raise ValueError(f"{source_file}: Missing '{key}'.")

    body = "\n".join(lines[body_start:]).lstrip()

    return metadata, body


def build_essay(template, metadata, body):
    html = template.replace(
        TITLE_PLACEHOLDER,
        f"{metadata['Title']} | Bravo Math"
    )

    html = html.replace(
        CONTENT_PLACEHOLDER,
        f"<h1>{metadata['Title']}</h1>\n\n"
        f'<p class="essay-date">{metadata["Date"]}</p>\n\n'
        f"{body}"
    )

    return html


def build_index(template, essays):
    items = []

    for essay in essays:
        items.append(
            f'<li><a href="essays/{essay["filename"]}">{essay["title"]}</a> '
            f'({essay["date"]})</li>'
        )

    return template.replace(INDEX_PLACEHOLDER, "<ul>\n" + "\n".join(items) + "\n</ul>")


def main():
    OUTPUT_DIR.mkdir(exist_ok=True)

    essay_template = TEMPLATE_FILE.read_text(encoding="utf-8")
    index_template = INDEX_TEMPLATE_FILE.read_text(encoding="utf-8")

    essays = []

    for source_file in SOURCE_DIR.glob("*.html"):
        metadata, body = read_essay(source_file)

        output = build_essay(essay_template, metadata, body)

        output_file = OUTPUT_DIR / source_file.name
        output_file.write_text(output, encoding="utf-8")

        essays.append({
            "title": metadata["Title"],
            "date": metadata["Date"],
            "filename": source_file.name,
            "sort_date": datetime.strptime(metadata["Date"], "%B %Y")
        })

    essays.sort(key=lambda e: e["sort_date"], reverse=True)

    index = build_index(index_template, essays)
    INDEX_FILE.write_text(index, encoding="utf-8")

    print(f"Generated {len(essays)} essay(s).")


if __name__ == "__main__":
    main()
