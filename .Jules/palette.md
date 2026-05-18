## 2024-11-20 - Avoid nesting <a> tags inside <button> elements
**Learning:** Nesting interactive elements like `<a>` tags inside `<button>` elements creates invalid HTML and completely breaks keyboard accessibility and screen reader support, as both are interactive elements.
**Action:** When a button needs to act as a link, use a semantic `<a>` tag and style it to look like a button, ensuring it includes interactive feedback styles like `:hover` and `:focus-visible` for keyboard navigation.
