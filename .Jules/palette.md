## 2026-04-09 - Replacing Invalid Nested Interactive Elements
**Learning:** Found nested interactive elements (`<button>` containing `<a>`) used for downloads. This breaks keyboard accessibility, focus management, and creates invalid HTML. Screen readers struggle with nested interactive roles.
**Action:** Replace native `<button>` elements with semantic `<a>` tags utilizing `display: inline-block` and define `:hover` and `:focus-visible` pseudo-classes to restore the visual interactive feedback native buttons provide. Use the `download` attribute for direct file downloads.
