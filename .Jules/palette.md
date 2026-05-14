## 2024-06-25 - Replace invalid nested buttons with styled semantic anchors
**Learning:** Nesting interactive elements like `<a>` inside `<button>` breaks keyboard accessibility and creates invalid HTML, making links unclickable or confusing for screen readers.
**Action:** When replacing native `<button>` elements with styled `<a>` tags to resolve accessibility constraints, always apply `display: inline-block` and define `:hover` and `:focus-visible` pseudo-classes to restore the visual interactive feedback native buttons provide.
