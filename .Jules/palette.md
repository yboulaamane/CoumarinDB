
## 2024-05-20 - Avoiding nested interactive elements
**Learning:** Nesting interactive elements like `<a>` inside `<button>` breaks keyboard accessibility and creates invalid HTML. When replacing native buttons with styled anchor tags to resolve these constraints, it's necessary to add `display: inline-block` and define `:hover` and `:focus-visible` pseudo-classes to restore the visual interactive feedback native buttons provide.
**Action:** Always apply `display: inline-block`, `:hover`, and `:focus-visible` when replacing native `<button>` elements with styled `<a>` tags.
