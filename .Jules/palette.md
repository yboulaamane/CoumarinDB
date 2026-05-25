## 2024-05-25 - Refactor download buttons to semantic links
**Learning:** Nesting interactive elements, such as `<a>` tags inside `<button>` tags, is an accessibility anti-pattern. This makes the underlying links undiscoverable to screen readers and prevents keyboard-only navigation via tabbing because native `<button>` elements mask the link behavior.
**Action:** Always use semantic `<a>` tags formatted to look like buttons via CSS classes (e.g. `display: inline-block`) when navigating to a URL or downloading a file, rather than nesting inside interactive wrapper elements.
