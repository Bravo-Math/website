from pathlib import Path

# Files and folders
TEMPLATE_FILE = "c2c-template.html"
OUTPUT_FILE = "c2c.html"
CURRICULUM_DIR = Path("c2c-curriculum")

# Courses, in Counting to Calculus order
COURSES = [

    ("preface.html", "Preface"),
    
    ("learning101.html", "Learning 101"),

    ("integers1.html", "Integers 1: How Many?"),
    ("integers2.html", "Integers 2: Add & Subtract within 100"),
    ("integers3.html", "Integers 3: Multiply and Divide within 100"),
    ("integers4.html", "Integers 4: All Operations within 100"),
    ("integers5.html", "Integers 5: Place Value"),
    ("integers6.html", "Integers 6: Negativity"),

    ("fractions1.html", "Fractions 1: Fractions are Numbers"),
    ("fractions2.html", "Fractions 2: Whole & Fraction Arithmetic"),
    ("fractions3.html", "Fractions 3: Fraction & Fraction Arithmetic"),
    ("fractions4.html", "Fractions 4: Rational Numbers"),

    ("algebra1.html", "Algebra 1: Solutions & Equality"),
    ("algebra2.html", "Algebra 2: Recursion & Linear Relations"),
    ("algebra3.html", "Algebra 3: Functions"),

    ("calculus.html", "Calculus"),

    ("statistics.html", "Statistics"),

    ("scholarsinschool.html", "Scholars in School"),
]

PLACEHOLDER = "<!-- BUILD-C2C:CURRICULUM -->"


def build_course(title, body):
    return f"""
<section class="box course">

    <div class="toggler">{title}</div>

    <div class="panel">
{body}
    </div>

</section>
"""


def main():
    template = Path(TEMPLATE_FILE).read_text(encoding="utf-8")

    curriculum = ""

    for filename, title in COURSES:
        path = CURRICULUM_DIR / filename

        if not path.exists():
            continue

        body = path.read_text(encoding="utf-8").strip()

        curriculum += "\n\n" + build_course(title, body)

    output = template.replace(PLACEHOLDER, curriculum)

    Path(OUTPUT_FILE).write_text(output, encoding="utf-8")

    print(f"Built {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
