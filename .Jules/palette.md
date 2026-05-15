
## 2024-05-19 - Invalid nested interactive elements (<a> inside <button>)
**Learning:** Avoid nesting interactive elements like `<a>` inside `<button>` elements, as it breaks keyboard accessibility, screen reader logic, and creates invalid HTML.
**Action:** When buttons just need to link somewhere, apply CSS classes to semantic `<a>` tags instead of using native `<button>` tags. Apply `display: inline-block` and define `:hover` and `:focus-visible` to restore the visual interactive feedback.
