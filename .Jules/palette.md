## 2024-04-19 - Semantic Download Buttons
**Learning:** Nesting interactive elements (`<a>` inside `<button>`) breaks keyboard accessibility and creates invalid HTML. Furthermore, using absolute GitHub blob URLs for downloads bypasses the HTML5 `download` attribute functionality.
**Action:** Replace nested `<button><a>` constructs with semantic `<a>` tags styled as buttons (`display: inline-block`), add `:hover` and `:focus-visible` pseudo-classes for interactive feedback, and use relative paths with the `download` attribute.
