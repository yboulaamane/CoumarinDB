## 2024-05-24 - Replacing Invalid Nested Interactive Elements
**Learning:** Using `<a>` inside `<button>` breaks keyboard navigation and creates invalid HTML, blocking screen readers. Additionally, pointing download links to GitHub blob URLs forces users to navigate away rather than downloading the file directly.
**Action:** Replace nested `<button><a>` with a single semantic `<a>` tag using `download` attribute and relative paths, and applying CSS classes with `:hover` and `:focus-visible` pseudo-classes to retain button-like interaction feedback.
