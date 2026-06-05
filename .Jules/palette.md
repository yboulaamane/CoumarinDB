## 2024-05-24 - Do not nest interactive elements
**Learning:** Found nested interactive elements (`<button>` containing `<a>`) used for download links in `index.html`. This is invalid HTML and creates significant accessibility issues: screen readers may announce both elements confusingly, and tab navigation can become unpredictable.
**Action:** Replaced the nested structure with a single semantic `<a>` tag. Used `role="button"` and CSS classes to preserve the visual appearance of a button while maintaining proper semantics and accessibility. Added descriptive `aria-label`s.
