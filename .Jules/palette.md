## 2024-05-03 - Avoid nesting interactive elements
**Learning:** Nesting `<a>` inside `<button>` creates invalid HTML and breaks keyboard accessibility. Screen readers and keyboard navigation struggle to interpret nested interactive elements correctly.
**Action:** Replace nested buttons with semantic `<a>` tags styled as buttons (using `display: inline-block`, `:hover`, and `:focus-visible` states) to preserve accessibility and valid HTML structure.
