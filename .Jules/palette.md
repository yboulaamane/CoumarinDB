## 2026-02-20 - Invalid Button Nesting
**Learning:** Detected `<button>` elements wrapping `<a>` tags for download actions. This nesting is invalid HTML and degrades accessibility for screen reader users who may not perceive the inner link or face interaction issues.
**Action:** When creating button-like links, use `<a>` tags with `role="button"` (if needed, though semantic `<a>` is often enough) and CSS styling, rather than nesting. Ensure `aria-label` is used if the text content isn't descriptive enough or if visual styling mimics a button.
