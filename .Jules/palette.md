## 2026-04-04 - Semantic Download Buttons
**Learning:** Nesting interactive elements like `<a>` inside `<button>` tags breaks keyboard accessibility and creates invalid HTML, while also preventing native interactive feedback (:hover, :focus-visible) on the anchor itself.
**Action:** Always replace `<button><a>` constructs with semantic `<a>` tags applying `display: inline-block` and button-like CSS (including `:hover` and `:focus-visible` states) to maintain valid HTML, ensure keyboard accessibility, and preserve visual interactivity.
