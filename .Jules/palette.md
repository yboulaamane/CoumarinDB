## 2024-06-15 - Fixed Nested Interactive Elements

**Learning:** This app's index.html used nested interactive elements (an `<a>` tag inside a `<button>` tag) for download links. This is invalid HTML and causes severe accessibility issues because screen readers and keyboard navigation get confused by two nested focusable elements.
**Action:** Replaced the nested `<button><a>...</a></button>` structure with a single semantic `<a>` tag styled to look like a button (`display: inline-block`, along with the existing button styles). Added `role="button"` and a descriptive `aria-label` to maintain accessibility and functionality.
