## 2026-02-17 - Button Nesting Anti-Pattern
**Learning:** Found critical a11y issue where `<a>` tags were nested inside `<button>` tags, creating invalid HTML and confusing screen readers.
**Action:** Refactored into semantic `<a>` tags with `.download-btn` class. Standardized this pattern for future action buttons.
