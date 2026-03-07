## 2026-03-07 - [Fixing button links and asset paths]
**Learning:** Using nested interactive elements like `<button><a>` is invalid HTML and harms accessibility. Additionally, relying on absolute GitHub URLs for assets restricts standard behavior (like HTML5 `download` attributes) and increases network overhead.
**Action:** Always use semantic `<a>` tags styled as buttons with relative paths and the `download` attribute for direct file downloads. Ensure images use descriptive `alt` text and relative paths for better accessibility and caching.
