## 2024-05-04 - Fix invalid nested interactive elements
**Learning:** Nesting interactive elements like `<a>` inside `<button>` breaks keyboard accessibility, screen reader compatibility, and creates invalid HTML.
**Action:** Always replace this pattern with semantic `<a>` tags formatted as buttons using CSS (e.g., `display: inline-block`) and ensure pseudo-classes `:hover` and `:focus-visible` are defined to restore visual interactive feedback. Also remember to add `rel="noopener noreferrer"` when using `target="_blank"`.
