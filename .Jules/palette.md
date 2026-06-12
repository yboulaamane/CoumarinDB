## 2024-06-12 - Accessibility fix for download buttons
**Learning:** Nested interactive elements (like `<a>` inside `<button>`) cause issues for screen readers. Using a semantic `<a>` tag with `role="button"` and a descriptive `aria-label` provides a much better experience while maintaining visual appearance.
**Action:** Replace `<a>` inside `<button>` with a single `<a>` tag styled as a button when creating download links.
