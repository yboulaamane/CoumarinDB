## 2024-05-18 - [Accessibility: Nested Interactive Elements]
**Learning:** Found nested interactive elements (`<a>` inside `<button>`) which is invalid HTML and causes issues for screen readers. A `<button>` should not contain interactive descendants.
**Action:** Replaced nested `<button>` + `<a>` combinations with a single semantic `<a>` tag with `role="button"` and `display: inline-block` to maintain the visual appearance of a button while ensuring accessibility and valid HTML.
