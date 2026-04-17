## 2024-04-17 - Button Accessibility and HTML Validity
**Learning:** Nesting interactive elements (like `<a>` inside `<button>`) breaks keyboard accessibility and creates invalid HTML. Also, using a `<title>` tag in `<head>` is required for screen readers.
**Action:** Replace nested buttons with semantic `<a>` tags styled as buttons (using CSS `display: inline-block` and focus/hover states) and ensure `<title>` is present in `<head>`.
