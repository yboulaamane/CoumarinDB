## 2024-05-19 - Semantic HTML for Download Links
**Learning:** Using an `<a>` tag inside a `<button>` tag for navigation or downloading files creates an invalid HTML structure and confusing accessibility tree for screen readers. The interactive semantics of `<button>` conflict with the navigation semantics of `<a>`.
**Action:** Replace nested `<button><a>...</a></button>` patterns with a single `<a>` tag styled to look like a button, and add `role="button"` and `aria-label` to ensure valid HTML and proper screen reader announcements.
