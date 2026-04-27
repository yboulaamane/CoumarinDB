## 2024-04-27 - Fixed semantic markup for download buttons
**Learning:** Avoid nesting interactive elements like `<a>` inside `<button>`. Use `<a>` styled as buttons directly.
**Action:** Replace `<button><a>...</a></button>` with `<a class="download-btn">...</a>` and use CSS to apply button styling, hover, and focus-visible states. Added `rel="noopener noreferrer"` for security.
