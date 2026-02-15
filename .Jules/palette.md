## 2026-02-15 - Fix Invalid Button Nesting
**Learning:** The codebase used `<button>` tags wrapping `<a>` tags for download links, which is invalid HTML and creates accessibility barriers.
**Action:** Replace such patterns with semantic `<a>` tags styled as buttons using CSS classes and proper ARIA labels.
