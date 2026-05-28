
## 2026-05-28 - Avoid nested interactive elements (button > a)
**Learning:** Found nested interactive elements (`<button><a>...</a></button>`) for download links. This is invalid HTML and creates accessibility issues because screen readers may announce both the button and the link, creating confusion, and keyboard navigation may be unpredictable.
**Action:** Replace nested `<button><a>` patterns with a semantic `<a>` tag styled as a button using CSS classes (e.g. `.download-btn`), and include `role="button"` and descriptive `aria-label`s.
