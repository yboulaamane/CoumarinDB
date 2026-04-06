## 2024-04-06 - Replacing nested button-links with semantic links
**Learning:** Using nested `<button><a href="...">...</a></button>` structures breaks keyboard accessibility and creates invalid HTML.
**Action:** Always replace these with semantic `<a>` tags styled with CSS. Ensure to add `display: inline-block` and define `:hover` and `:focus-visible` pseudo-classes to restore the visual interactive feedback native buttons provide. Use the HTML5 `download` attribute with relative paths for correct download behavior.
