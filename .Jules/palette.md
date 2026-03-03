## 2024-05-24 - Semantic Buttons for Downloads
**Learning:** Found `<button>` elements that wrap `<a>` tags. While this works visually, it's invalid HTML (interactive content cannot be a descendant of another interactive element) and creates a confusing experience for screen readers. Instead, we should style `<a>` tags to look like buttons, or use buttons with click handlers.
**Action:** When finding a link that looks like a button, use a styled `<a>` tag with appropriate classes rather than wrapping it in a `<button>` element.
