## 2026-06-17 - Screen Reader Issues with Nested Interactive Elements
**Learning:** Screen readers struggle to correctly interpret and navigate when interactive elements are nested, such as placing an `<a>` tag inside a `<button>` tag. This invalid HTML causes confusion and poor accessibility.
**Action:** Use semantic `<a>` tags with `role="button"`, `display: inline-block`, and descriptive `aria-label` attributes to create accessible download links that look like buttons.
