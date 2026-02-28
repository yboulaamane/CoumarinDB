## 2024-05-24 - Semantic Links over Buttons
**Learning:** In a previous project with similar layout, placing anchor tags (`<a>`) inside `<button>` elements caused HTML validation errors and accessibility issues, as interactive elements shouldn't be nested. Screen readers were confused about the role (button vs link).
**Action:** When creating styled links that look like buttons, use semantic `<a>` tags with a CSS class to style them like buttons, rather than nesting `<a>` inside `<button>`.

## 2024-05-25 - Target Blank Security
**Learning:** Using `target="_blank"` on links without `rel="noopener noreferrer"` can create a security vulnerability called Reverse Tabnabbing, and it also impacts performance.
**Action:** Always include `rel="noopener noreferrer"` on external links that open in a new tab.

## 2024-05-26 - Download Button Accessibility
**Learning:** Found nested `<a>` inside `<button>` elements, which is invalid HTML and causes screen readers to misinterpret the element's role. Missing hover/focus states also hindered keyboard accessibility.
**Action:** Replaced nested structures with semantic `<a>` tags styled as buttons (`.download-btn`), adding `aria-label`s, `rel="noopener noreferrer"`, and proper `:hover` / `:focus-visible` CSS states.
