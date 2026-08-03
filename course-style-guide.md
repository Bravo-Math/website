# Bravo Math Course Style Guide
This document defines the standards for all Bravo Math curriculum pages.
Its purpose is to ensure every course feels like it belongs to the same website, regardless of when it was created.
## Philosophy
A Bravo Math course is **not** a Moodle export.
It is a polished web page designed for students.
When converting content:
- Preserve educational meaning.
- Improve readability.
- Prefer simplicity.
- Maintain consistency.
## The Role of AI
AI should act as an editor and web designer, not a mechanical converter.
Responsibilities include:
- Simplifying HTML.
- Improving organization.
- Improving visual hierarchy.
- Improving scanability.
- Improving consistency.
- Recommending improvements.
Suggestions are encouraged whenever they improve the curriculum.
## Reference Implementation
The latest version of `learning101.html` is the reference implementation.
Future courses should feel like they were written alongside it.
## HTML Structure
### H1
Never use H1 within course content.
### Course Title
The course title is displayed by the course accordion.
Do not duplicate it inside the page.
### H2
Use H2 for major sections.
Examples:
- Introduction
- Resources
- Practice
- Solving Equations
- Applications
A student should be able to understand the page's organization simply by reading the H2 headings.
### H3
Use H3 for subsections within an H2.
Examples:
- Videos
- Worksheets
- Discussion
- Calculator
- Examples
### H4
Never use H4.
If another level of organization is needed, prefer:
```html
<p><strong>Heading</strong></p>
```
Only use this when it genuinely improves readability.
## Paragraphs
Paragraphs are the default.
- Avoid breaking ideas into many tiny paragraphs.
- Prefer concise paragraphs over large walls of text.
## Bold
Use bold sparingly.
Good uses:
- Introducing a small subsection.
- Emphasizing an important label.
- Highlighting a key idea.
If everything is bold, nothing is bold.
## Lists
Use lists only when they genuinely improve readability.
Good uses:
- Steps.
- Resources.
- Comparisons.
- Checklists.
Avoid deeply nested lists whenever possible.
## Tables
Use tables only when they help compare information.
Never use tables for layout.
## Links
Use descriptive link text.
Good:
- Learning Scientists
- Desmos Graphing Calculator
Poor:
- Click here
- More
## Images
Images should appear near the relevant content.
Images should support learning rather than decorate the page.
Always include meaningful `alt` text.
## Videos
Group related videos together.
Avoid scattering individual videos throughout a page.
## Resources
Group similar resources together.
Example:
```
Calculators
- Desmos
- Symbolab
- Wolfram Alpha
```
instead of scattering them throughout the page.
## Moodle Conversion
Do not preserve Moodle structure unless it improves the page.
Allowed:
- Reorganizing sections.
- Combining related material.
- Simplifying nesting.
- Removing unnecessary formatting.
Not allowed:
- Changing educational meaning.
- Removing important content.
- Rewriting technical explanations.
## HTML
Prefer semantic HTML.
Use:
- Headings.
- Paragraphs.
- Lists.
- Tables.
Avoid unnecessary `<div>` elements.
Avoid inline styles.
## CSS
Prefer reusable CSS.
If a pattern appears multiple times, recommend creating a reusable CSS class.
Recommend global CSS improvements whenever they benefit multiple courses.
## Accessibility
- Maintain a logical heading hierarchy.
- Use descriptive links.
- Use tables only for tabular data.
- Include meaningful `alt` text for images.
## Editorial Principles
Before producing HTML, ask:
- Can this be simpler?
- Can this be easier to scan?
- Can this be more semantic?
- Can this be more consistent?
- Would a student understand this more quickly?
## Suggestions
Suggestions are encouraged.
Recommend improvements involving:
- HTML.
- CSS.
- Typography.
- Navigation.
- Accessibility.
- Organization.
- User experience.
Optimize the website as a whole, not just the current page.
## Guiding Principle
Optimize for consistency over perfection.
Every course should feel like part of the same curriculum.
Small improvements that benefit every future course are usually more valuable than perfecting a single page.
Always decide on the best information architecture before writing HTML.
Do not mechanically translate Moodle line by line.
