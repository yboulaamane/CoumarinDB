## 2024-06-06 - Replacing nested interactive elements (a inside button) for accessibility

**Learning:** `<a>` elements inside `<button>` elements represent nested interactive controls, which is invalid HTML and causes severe issues for screen readers. Screen readers may announce both elements confusingly or fail to activate the intended link.

**Action:** When implementing download links or actions that navigate, strictly use `<a>` tags styled as buttons (with `role="button"` and clear `aria-label`s) rather than nesting `<a>` inside `<button>`. Added `display: inline-block` and `margin` for proper layout when converting block-level buttons to inline anchor tags.
