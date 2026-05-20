## 2024-05-20 - Refactoring Nested Interactive Elements
**Learning:** Nesting interactive elements (like `<a>` inside `<button>`) results in invalid HTML and severely breaks screen reader navigation, as screen readers struggle to announce the correct interaction intent.
**Action:** Replace nested `<button><a>...</a></button>` patterns with semantic `<a>` tags styled as buttons. Always ensure that visual interactive feedback is retained by defining `:hover` and `:focus-visible` pseudo-classes on the new class.
