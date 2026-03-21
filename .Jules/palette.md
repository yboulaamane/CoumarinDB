## 2024-05-28 - Avoid Invalid HTML Nesting and Use Direct Downloads
**Learning:** Nesting interactive elements like `<a>` inside `<button>` breaks keyboard accessibility and produces invalid HTML. Using absolute GitHub blob URLs for static files opens them in a new tab instead of initiating a download.
**Action:** Use semantic `<a>` tags with CSS classes applied for button styling. Use relative URLs combined with the `download` attribute to allow direct file downloads without navigating away or opening new tabs.
