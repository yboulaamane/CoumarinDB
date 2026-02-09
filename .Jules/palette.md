## 2025-02-09 - Accessibility Trap: Buttons vs Links
**Learning:** Found a common anti-pattern where `<a>` tags were wrapped in `<button>` elements to achieve a button-like appearance. This is invalid HTML and confuses screen readers.
**Action:** Always replace `<button><a>` with `<a>` styled as a button. If the element navigates, it's a link. If it performs an action, it's a button.
