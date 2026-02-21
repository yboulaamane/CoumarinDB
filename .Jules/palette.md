## 2026-02-21 - Invalid Button Nesting for Links
**Learning:** Found multiple instances of `<button>` elements wrapping `<a>` tags for primary actions (Downloads). This is invalid HTML and causes UX issues where clicking the button padding (outside the anchor's text) triggers no action, frustrating users. It also confuses screen readers.
**Action:** Always replace `<button><a>...</a></button>` patterns with styled `<a>` tags (`display: inline-block` or `inline-flex`) to ensure the entire visual area is clickable and semantically correct.
