## 2024-05-24 - Invalid Button/Anchor Nesting
**Learning:** Found invalid HTML nesting in `index.html` where `<a>` tags were wrapped inside `<button>` elements. This breaks keyboard accessibility and screen readers, as buttons and links have conflicting roles and focus behaviors.
**Action:** Replaced the invalid structure with semantic `<a>` tags, using a custom CSS class (`.download-btn`) to maintain button-like visual styling, including `:hover` and `:focus-visible` states for proper interactive feedback.
