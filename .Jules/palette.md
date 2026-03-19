## Palette's Journal

## 2024-11-20 - Invalid nested interactive elements for styling
**Learning:** In static pages, download links are sometimes invalidly nested inside `<button>` tags (e.g., `<button><a>...</a></button>`) to achieve a button-like appearance. This creates invalid HTML and breaks keyboard accessibility for screen readers.
**Action:** Replace the nested structure with semantic `<a>` tags and use a dedicated CSS class (e.g., `.download-btn`) to apply the button styling while preserving standard link behavior and accessibility.
