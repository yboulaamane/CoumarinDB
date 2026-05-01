
## 2024-05-01 - Avoid nesting interactive elements
**Learning:** Nesting interactive elements (like an `<a>` inside a `<button>`) results in invalid HTML and breaks keyboard navigation/screen reader support.
**Action:** Replace nested `<button><a>...</a></button>` markup with semantic `<a class="btn">...</a>` tags, using CSS (`display: inline-block`, `:hover`, `:focus-visible`) to restore the visual interactive feedback native buttons provide.
