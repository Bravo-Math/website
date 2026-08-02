#!/usr/bin/env python3

"""
Builds c2c.html from:

    c2c-template.html

and the course files inside:

    c2c-curriculum/

The generated file should never be edited directly.
Edit the template or the individual course files instead.
"""

from pathlib import Path


# ------------------------------------------------------------
# Files and folders
# ------------------------------------------------------------

ROOT = Path(__file__).parent

TEMPLATE_FILE = ROOT / "c2c-template.html"
OUTPUT_FILE = ROOT / "c2c.html"

c2c-curriculum_FOLDER = ROOT / "c2c-curriculum"


# ------------------------------------------------------------
# c2c-curriculum order
#
# This list defines the exact order students see the courses.
# ------------------------------------------------------------

COURSES = [

    "learning101.html",

    "integers1.html",
    "integers2.html",
    "integers3.html",
    "integers4.html",
    "integers5.html",
    "integers6.html",

    "fractions1.html",
    "fractions2.html",
    "fractions3.html",
    "fractions4.html",

    "algebra1.html",
    "algebra2.html",
    "algebra3.html",

    "calculus.html",

    "statistics.html",

    "scholars-in-school.html",
]


# ------------------------------------------------------------
# Read the template
# ------------------------------------------------------------

print("Reading template...")

template = TEMPLATE_FILE.read_text(encoding="utf-8")


# ------------------------------------------------------------
# Build the c2c-curriculum
# ------------------------------------------------------------

print("Building c2c-curriculum...\n")

c2c-curriculum = ""

for filename in COURSES:

    filepath = c2c-curriculum_FOLDER / filename

    if not filepath.exists():
        raise FileNotFoundError(
            f"\nMissing c2c-curriculum file:\n\n{filepath}"
        )

    print(f"✓ {filename}")

    course = filepath.read_text(encoding="utf-8")

    c2c-curriculum += (
        "\n\n"
        "<!-- ========================================================== -->\n"
        f"<!-- {filename} -->\n"
        "<!-- ========================================================== -->\n\n"
        + course
    )


# ------------------------------------------------------------
# Replace the placeholder
# ------------------------------------------------------------

PLACEHOLDER = "<!-- BUILD:c2c-curriculum -->"

if PLACEHOLDER not in template:
    raise ValueError(
        f"\nCould not find placeholder:\n\n{PLACEHOLDER}"
    )

output = template.replace(PLACEHOLDER, c2c-curriculum)


# ------------------------------------------------------------
# Save c2c.html
# ------------------------------------------------------------

OUTPUT_FILE.write_text(output, encoding="utf-8")

print("\nFinished.")
print("Generated c2c.html")
