## 2025-02-18 - Invalid Button Nesting
**Learning:** Found `<a>` tags nested inside `<button>` elements in `index.html`. This pattern is invalid HTML and confusing for screen readers, as it nests interactive elements.
**Action:** Always refactor to semantic `<a>` tags with button-like styling (CSS classes) and appropriate ARIA roles/labels if needed.
