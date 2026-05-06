## 2024-05-06 - Semantic download buttons
**Learning:** Replacing native HTML `<button>` wrapping an `<a>` tag with semantic styled `<a>` elements resolves significant accessibility constraints by preventing nested interactive elements and restoring proper keyboard navigation, focus, and interactive visual feedback.
**Action:** Always prefer applying visual button styles directly to semantic `<a>` tags via CSS classes, combined with `:hover` and `:focus-visible` pseudo-classes to emulate native button interactions instead of structurally wrapping links in unstyled buttons.
