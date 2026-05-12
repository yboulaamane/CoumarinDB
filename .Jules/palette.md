## 2026-05-12 - Refactored Nested Interactive Elements for Accessibility
**Learning:** Found `<button>` elements containing nested `<a>` elements for download links. This is a severe accessibility anti-pattern as interactive elements cannot be nested in HTML, leading to screen reader confusion and broken keyboard navigation.
**Action:** Replaced the `<button>` tags with semantic `<a>` tags and styled them to look like buttons using CSS (`.download-btn` class with `display: inline-block`, `:hover`, and `:focus-visible` states) to ensure proper keyboard operability and valid HTML.
