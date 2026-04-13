## 2026-04-13 - Accessible Download Links

**Learning:** Nesting `<a>` inside `<button>` tags creates invalid HTML and breaks keyboard accessibility. When replacing native `<button>` elements with styled `<a>` tags to resolve accessibility constraints, always apply `display: inline-block` and define `:hover` and `:focus-visible` pseudo-classes to restore the visual interactive feedback native buttons provide. Additionally, using relative paths with the HTML5 `download` attribute ensures direct file downloads bypass the GitHub web interface and correctly prompt the user.

**Action:** Replace unsemantic `<button><a>...</a></button>` wrappers with semantic `<a href="./..." class="download-btn" download>...</a>`. Ensure the `.download-btn` class includes `display: inline-block` and appropriate pseudo-class styles for interaction feedback.
