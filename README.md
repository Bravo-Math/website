# Bravo Math Website

Official website for Bravo Math.

---

# What should I edit?

## Edit directly

* index.html
* about.html
* library.html
* contact.html
* jobs.html
* style.css
* essay-template.html
* c2c-template.html
* build-essays.py
* build-c2c.py
* Anything inside `essays-source/`
* Anything inside `c2c-curriculum/`

---

## Never edit directly

These files are generated automatically.

* Anything inside `essays/`
* c2c.html

Edit their source files instead.

---

# Directory Structure

```
.
├── about.html
├── contact.html
├── jobs.html
├── library.html
├── index.html
│
├── c2c-template.html
├── c2c.html
├── c2c-curriculum/
│
├── essay-template.html
├── essays/
├── essays-source/
│
├── images/
├── favicons/
│
├── build-c2c.py
├── build-essays.py
│
├── style.css
└── README.md
```

---

# Philosophy

Keep the website simple.

Whenever possible:

* Edit source files, not generated files.
* Automate repetitive work.
* Avoid unnecessary automation.
* Prefer simple architecture over clever architecture.

---

# HTML Standard

Every page follows the same `<head>`.

## Required customization

* `<title>`
* `<meta name="description">`

Everything else should remain identical.

---

# Counting to Calculus

Never edit:

```
c2c.html
```

The individual curriculum pages are stored in:

```
c2c-curriculum/
```

The C2C build script assembles those pages using:

```
build-c2c.py
```

The overall page structure is controlled by:

```
c2c-template.html
```

Edit the appropriate source file, then rebuild.

---

# Essays

Never edit anything inside:

```
essays/
```

Instead:

1. Edit or create a file in:

```
essays-source/
```

2. Commit the changes.

GitHub Actions automatically rebuilds the published essay pages.

---

# Library

`library.html` is maintained manually.

Sections:

* Latest Updates
* Resources
* Essays

Only the essay pages are generated.

---

# GitHub Actions

The essay build workflow runs whenever one of these changes:

* `essay-template.html`
* `build-essays.py`
* anything inside `essays-source/`

It regenerates the contents of:

```
essays/
```

It never edits `library.html`.

The Counting to Calculus build workflow rebuilds:

```
c2c.html
```

from the C2C source files and build files.

---

# Future Ideas

Possible future improvements:

* Generate essay descriptions automatically.
* Organize essays by topic.
* Improve SEO.
* Redirect obsolete URLs.
* Student login.
* Assignment submission.
* Progress tracking.
* Site search.
