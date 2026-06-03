## 2024-06-03 - Invalid Button Nesting with Download Links
**Learning:** This app previously used `<a>` tags nested directly inside `<button>` tags for downloads, which creates conflicting interactive semantics for screen readers and breaks keyboard navigation (as focus attempts to land on both the button and the link).
**Action:** When adding or refactoring download actions, always use semantic `<a>` tags styled as buttons with `role="button"` and `aria-label`s, rather than nesting interactive elements.
