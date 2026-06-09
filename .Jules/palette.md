## 2024-06-25 - Prevent Nested Interactive Controls in Download Buttons
**Learning:** Found `<button>` elements wrapping `<a>` tags for download links. This is a critical accessibility anti-pattern because screen readers and keyboard navigation struggle with nested interactive elements (they may read it twice, skip it, or fail to activate properly).
**Action:** Always use a semantic `<a>` tag with `role="button"` (and descriptive `aria-label`) for links that look like buttons, rather than nesting them. Combine styles onto the anchor tag directly.
