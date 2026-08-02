#!/usr/bin/env python3

"""
Build c2c.html from:

    c2c-template.html

and the course files inside:

    c2c-curriculum/

The generated c2c.html should never be edited directly.
Edit the template or the individual course files instead.
"""

from pathlib import Path


# ============================================================
# Files and folders
# ============================================================

ROOT = Path(__file__).parent

TEMPLATE_FILE = ROOT / "c2c-template.html"
OUTPUT_FILE = ROOT / "c2c.html"

C2C_CURRICULUM_FOLDER = ROOT / "c2c-curriculum"


# ============================================================
# Course order
#
# This list defines the exact order students see the courses.
# Missing files are skipped until you create them.
# ============================================================

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


# ============================================================
# Read the template
# ============================================================

print("Reading template...")

if not TEMPLATE_FILE.exists():
    raise FileNotFoundError(
        f"Could not find template:\n\n{TEMPLATE_FILE}"
    )

template = TEMPLATE_FILE.read_text(encoding="utf-8")


# ============================================================
# Build curriculum
# ============================================================

print("Building curriculum...\n")

curriculum = ""

for filename in COURSES:

    filepath = C2C_CURRICULUM_FOLDER / filename

    if not filepath.exists():
        print(f"Skipping {filename}")
        continue

    print(f"✓ {filename}")

    course = filepath.read_text(encoding="utf-8").strip()

    curriculum += (
        "\n\n"
        "<!-- ========================================================== -->\n"
        f"<!-- {filename} -->\n"
        "<!-- ========================================================== -->\n\n"
        + course
    )


# ============================================================
# Replace placeholder
# ============================================================

PLACEHOLDER = "<!-- BUILD-C2C:CURRICULUM -->"

if PLACEHOLDER not in template:
    raise ValueError(
        f"Could not find placeholder:\n\n{PLACEHOLDER}"
    )

output = template.replace(PLACEHOLDER, curriculum)


# ============================================================
# Write c2c.html
# ============================================================

OUTPUT_FILE.write_text(output, encoding="utf-8")

print("\nFinished.")
print(f"Generated {OUTPUT_FILE.name}")
