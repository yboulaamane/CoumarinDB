## 2024-05-08 - Fix Invalid Nested Interactive Elements
**Learning:** Nesting interactive elements (`<a>` inside `<button>`) breaks keyboard accessibility and creates invalid HTML.
**Action:** Replace nested `<button><a>` structures with semantic `<a>` tags styled to look and behave like buttons (using CSS classes for `display: inline-block`, `:hover`, and `:focus-visible` to retain expected interactive feedback).
