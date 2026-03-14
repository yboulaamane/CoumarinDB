## 2024-05-15 - Interactive Element Nesting
**Learning:** Nesting `<a>` tags inside `<button>` elements creates invalid HTML that confuses screen readers and breaks keyboard navigation, as both are interactive elements fighting for focus.
**Action:** Always use semantic `<a>` tags styled as buttons with CSS when the action is navigation or file download, reserving `<button>` for in-page actions and forms.
