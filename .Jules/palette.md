## 2024-03-26 - Accessible Semantic Download Buttons
**Learning:** Avoid wrapping anchor tags inside native `<button>` tags for downloads. It breaks keyboard accessibility, is invalid HTML, and screen readers struggle with it.
**Action:** Always use styled semantic `<a>` tags with `display: inline-block` and define `:hover` and `:focus-visible` pseudo-classes to restore the visual interactive feedback native buttons provide. Use `rel="noopener noreferrer"` with `target="_blank"`, and use relative paths for immediate downloading instead of linking to GitHub blobs which intercepts the download.
