## 2026-02-23 - Nested Interactive Elements
**Learning:** The application used `<a>` tags nested within `<button>` elements for download links. This is invalid HTML and causes accessibility issues for screen readers and unpredictable click behavior.
**Action:** Replace nested `<button><a>` structures with styled `<a>` tags (using `display: inline-block` and button-like styling) to maintain visual appearance while ensuring semantic validity and accessibility.
