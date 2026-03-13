## 2023-10-27 - Semantic Download Buttons & Accessibility
**Learning:** The previous `<button><a>...</a></button>` nesting was invalid HTML and posed accessibility challenges. Inline styles made maintenance difficult. Missing `alt` tags on key header images degrade the screen reader experience.
**Action:** Use semantic `<a class="download-btn">` tags styled as buttons for file downloads, ensuring the `download` attribute and relative paths are used so the user downloads the file directly without navigating away. Always ensure `<img src="...">` includes an `alt` attribute.
