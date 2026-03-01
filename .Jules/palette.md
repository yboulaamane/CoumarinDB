## 2024-05-24 - Initial Setup
**Learning:** Initialized palette journal.
**Action:** None.
## 2026-03-01 - Fix Invalid Interactive Element Nesting
**Learning:** Discovered an accessibility issue specific to this app where download links (`<a>`) were nested inside `<button>` tags. This invalid HTML structure causes severe navigation issues for screen reader and keyboard users.
**Action:** Replaced the nested `<button><a>` elements with semantic `<a>` tags, adding the `download-btn` class to style them like buttons, ensuring correct focus states and relative paths.
