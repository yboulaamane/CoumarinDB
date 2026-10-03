## 2024-10-03 - Screen reader announcements for dynamic text
**Learning:** Dynamic temporary text feedback elements (like copy buttons changing to "Copied" and then reverting) need `aria-live="polite"` to announce state changes to screen readers properly.
**Action:** Add `aria-live="polite"` to UI elements that update text temporarily.
