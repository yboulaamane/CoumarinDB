## 2024-04-21 - Accessible Download Buttons
**Learning:** Avoid nesting interactive elements like `<a>` inside `<button>`. Doing so breaks keyboard accessibility and creates invalid HTML. Furthermore, to enable HTML5's `download` attribute functionality effectively, links must use relative paths rather than absolute URLs.
**Action:** Replace invalid `<button><a>...</a></button>` nested patterns with appropriately styled `<a href="..." download class="...">` elements that restore button-like visual and interactive feedback through pseudo-classes (`:hover` and `:focus-visible`).
