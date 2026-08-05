from pathlib import Path
from datetime import datetime

# Files and folders
TEMPLATE_FILE = "essay-template.html"
OUTPUT_DIR = Path("essays")
INDEX_FILE = "essays.html"
ESSAYS_DIR = Path("essays-source")

TITLE_PLACEHOLDER = "<!-- BUILD-ESSAYS:TITLE -->"
CONTENT_PLACEHOLDER = "<!-- BUILD-ESSAYS:CONTENT -->"


def main():
    template = Path(TEMPLATE_FILE).read_text(encoding="utf-8")

    OUTPUT_DIR.mkdir(exist_ok=True)

    essays = []

    for path in ESSAYS_DIR.glob("*.html"):

        text = path.read_text(encoding="utf-8")

        if not text.startswith("<!--"):
            raise ValueError(f"{path.name}: Missing metadata block.")

        metadata_text, body = text.split("-->", 1)

        metadata = {}

        for line in metadata_text.splitlines():
            if ":" in line:
                key, value = line.split(":", 1)
                metadata[key.strip()] = value.strip()

        title = metadata["Title"]
        date = metadata["Date"]
        tags = metadata.get("Tags", "")

        output = template

        output = output.replace(
            TITLE_PLACEHOLDER,
            f"{title} | Bravo Math"
        )

        output = output.replace(
            CONTENT_PLACEHOLDER,
            f"<h1>{title}</h1>\n\n"
            f'<p class="essay-date">{date}</p>\n\n'
            f"{body.strip()}"
        )

        (OUTPUT_DIR / path.name).write_text(
            output,
            encoding="utf-8"
        )

        essays.append({
            "title": title,
            "date": date,
            "tags": tags,
            "filename": path.name,
            "sort_date": datetime.strptime(date, "%B %Y")
        })

    essays.sort(
        key=lambda essay: essay["sort_date"],
        reverse=True
    )

    index = """<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Essays | Bravo Math</title>

    <link rel="stylesheet" href="style.css">
</head>

<body>

<header>

    <div class="logo">
        <a href="/index.html">Bravo Math <img src="/images/shapes.png" class="shapes" alt=""></a>
    </div>

    <nav>
        <a href="/about.html" class="button">About</a>
        <a href="/c2c.html" class="button">Counting to Calculus</a>
        <a href="/essays.html" class="current button">Essays</a>
        <a href="/contact.html" class="button">Contact</a>
        <a href="/jobs.html" class="button">Jobs</a>
    </nav>

</header>

<main class="essay">

<h1>Essays</h1>

<ul>
"""

    for essay in essays:
        index += f"""
    <li>
        <a href="essays/{essay['filename']}">{essay['title']}</a><br>
        <span class="essay-date">{essay['date']}</span>
    </li>
"""

    index += """
</ul>

</main>

</body>
</html>
"""

    Path(INDEX_FILE).write_text(
        index,
        encoding="utf-8"
    )

    print(f"Built {len(essays)} essay(s).")


if __name__ == "__main__":
    main()
