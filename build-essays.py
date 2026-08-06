from pathlib import Path

# Files and folders
TEMPLATE_FILE = "essay-template.html"
OUTPUT_DIR = Path("essays")
ESSAYS_DIR = Path("essays-source")

TITLE_PLACEHOLDER = "<!-- BUILD-ESSAYS:TITLE -->"
CONTENT_PLACEHOLDER = "<!-- BUILD-ESSAYS:CONTENT -->"


def main():
    template = Path(TEMPLATE_FILE).read_text(encoding="utf-8")

    OUTPUT_DIR.mkdir(exist_ok=True)

    # Delete all previously generated essay pages.
    # The output directory should always be an exact mirror of essays-source.
    for output_file in OUTPUT_DIR.glob("*.html"):
        output_file.unlink()
    
    count = 0

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

        count += 1

    print(f"Built {count} essay(s).")


if __name__ == "__main__":
    main()
