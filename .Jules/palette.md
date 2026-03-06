## 2024-05-15 - Improve Download Links with Semantic HTML

**Learning:** When dealing with download buttons, wrapping `<a>` elements inside `<button>` tags is invalid HTML and can cause accessibility issues for screen readers. Further, external links to GitHub blob URLs do not trigger native file downloads, but rather navigate users to an external website, breaking the flow.
**Action:** Replace `<button><a>` patterns with semantic `<a class="download-btn" download>` attributes. Always use relative or local URLs instead of raw GitHub links when providing static file downloads in an interface to ensure a native, in-browser download experience without navigating away. Provide `:hover` and `:focus-visible` styles for better keyboard and mouse interaction feedback.
