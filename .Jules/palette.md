# Palette's Journal

## 2024-10-12 - [Invalid Button Nesting]
**Learning:** Found `<button><a>...</a></button>` pattern in `index.html`. This is invalid HTML and confusing for screen readers as it creates nested interactive controls.
**Action:** Always refactor to a single styled `<a>` tag and ensure `aria-label` is present for clarity.
