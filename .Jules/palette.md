## 2024-04-29 - Invalid Nested Interactive Elements
**Learning:** Nesting `<a>` tags inside `<button>` elements creates invalid HTML, breaking keyboard navigation and screen reader support, as both are interactive elements.
**Action:** Replace `<button>` wrappers with semantic `<a>` tags styled using CSS to look like buttons, ensuring `display: inline-block` and adding interactive states (`:hover`, `:focus-visible`) to restore the visual feedback of native buttons.
