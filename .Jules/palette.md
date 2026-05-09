## 2024-05-09 - Accessible Download Buttons
**Learning:** Nesting interactive elements like `<a>` inside `<button>` creates invalid HTML and severely impairs accessibility, breaking screen reader navigation and keyboard interactions.
**Action:** When styled buttons are needed for links, apply CSS classes (with interactive states like `:hover` and `:focus-visible`) directly to semantic `<a>` tags instead of wrapping them in `<button>` elements. Ensure appropriate `aria-label` or visually hidden text is present if the link relies on context.
