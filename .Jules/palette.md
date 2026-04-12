## 2024-04-12 - Semantic HTML for Download Actions
**Learning:** Nesting interactive elements (`<a>` inside `<button>`) is an accessibility anti-pattern that breaks keyboard navigation and screen readers. Additionally, linking to GitHub blob URLs for data files fails to trigger actual downloads.
**Action:** Always use semantic `<a>` tags with the `download` attribute and relative paths for direct file downloads, and apply CSS classes (`display: inline-block`, `:hover`, `:focus-visible`) to achieve button styling while preserving accessibility.
