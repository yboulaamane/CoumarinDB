## 2024-04-18 - Fix interactive element nesting

**Learning:** Nesting interactive elements (like `<a>` tags inside `<button>` tags) creates invalid HTML and breaks keyboard navigation and screen readers. Users cannot properly focus or interact with nested interactive elements.
**Action:** Always replace nested buttons/links with a single semantic `<a>` tag that uses CSS classes to provide button-like styling and interactive states (`:hover`, `:focus-visible`).
