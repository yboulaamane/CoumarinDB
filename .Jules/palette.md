## 2024-05-24 - Do not nest interactive elements
**Learning:** Nesting `<a>` inside `<button>` breaks keyboard accessibility and creates invalid HTML, particularly for visually styled download buttons.
**Action:** Replace `<button>` wrappers containing `<a>` tags with styled semantic `<a>` tags using `display: inline-block` and CSS classes for hover/focus states to preserve interactive feedback.
