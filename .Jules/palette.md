## 2024-04-25 - Avoid Invalid Nested Interactive Elements
**Learning:** When creating custom button styles for links that open in a new tab, avoid nesting `<a>` tags inside `<button>` elements as it breaks HTML validation and keyboard accessibility.
**Action:** Replace nested `<button><a>` elements with semantic `<a>` tags and apply custom CSS classes like `.download-btn` that mimic the visual appearance of buttons, complete with `:hover` and `:focus-visible` states to preserve interactive feedback.
