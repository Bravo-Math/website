from pathlib import Path
from datetime import datetime

TEMPLATE_FILE = Path("essay-template.html")
SOURCE_DIR = Path("essays-source")
OUTPUT_DIR = Path("essays")
INDEX_FILE = Path("essays.html")

TITLE_PLACEHOLDER = "<!-- BUILD-ESSAYS:TITLE -->"
CONTENT_PLACEHOLDER = "<!-- BUILD-ESSAYS:CONTENT -->"


def read_essay(source_file):
    lines = source_file.read_text(encoding="utf-8").splitlines()

    if not lines or lines[0].strip() != "<!--":
        raise ValueError(f"{source_file}: Missing metadata block.")

    metadata = {}
    body_start = None

    for i in range(1, len(lines)):
        line = lines[i].rstrip()

        if line == "-->":
            body_start = i + 1
            break

        if ":" in line:
            key, value = line.split(":", 1)
            metadata[key.strip()] = value.strip()

    if body_start is None:
        raise ValueError(f"{source_file}: Metadata block not closed.")

    for key in ("Title", "Date"):
        if key not in metadata:
            raise ValueError(f"{source_file}: Missing '{key}'.")

    body = "\n".join(lines[body_start:]).lstrip()

    return metadata, body


def build_essay(template, metadata, body):
    html = template

    html = html.replace(
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


def build_index(essays):
    html = """<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Essays | Bravo Math</title>

    <link rel="stylesheet" href="style.css">
</head>

<body>

<header>
    <nav>
        <a href="about.html" class="button">About</a>
        <a href="c2c.html" class="button">Counting to Calculus</a>
        <span class="current button">Essays</span>
        <a href="contact.html" class="button">Contact</a>
        <a href="jobs.html" class="button">Jobs</a>
    </nav>
</header>

<main class="essay">

<h1>Essays</h1>

<ul>
"""

    for essay in essays:
        html += f"""
    <li>
        <a href="essays/{essay['filename']}">{essay['title']}</a><br>
        <span class="essay-date">{essay['date']}</span>
    </li>
"""

    html += """
</ul>

</main>

</body>
</html>
"""

    return html


def main():
    OUTPUT_DIR.mkdir(exist_ok=True)

    template = TEMPLATE_FILE.read_text(encoding="utf-8")

    essays = []

    for source_file in SOURCE_DIR.glob("*.html"):

        metadata, body = read_essay(source_file)

        output = build_essay(template, metadata, body)

        output_file = OUTPUT_DIR / source_file.name
        output_file.write_text(output, encoding="utf-8")

        essays.append({
            "title": metadata["Title"],
            "date": metadata["Date"],
            "filename": source_file.name,
            "sort_date": datetime.strptime(metadata["Date"], "%B %Y")
        })

    essays.sort(
        key=lambda essay: essay["sort_date"],
        reverse=True
    )

    INDEX_FILE.write_text(
        build_index(essays),
        encoding="utf-8"
    )

    print(f"Generated {len(essays)} essay(s).")


if __name__ == "__main__":
    main()
