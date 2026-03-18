## 2024-05-23 - Interactive Elements Inside Buttons
**Learning:** Placing interactive elements like `<a>` tags inside `<button>` elements breaks keyboard accessibility and creates invalid HTML that fails with screen readers. This pattern is often mistakenly used to quickly style a link as a button.
**Action:** Always use CSS classes on semantic `<a>` tags to achieve "button" styling for links, preserving keyboard focus, `download` attributes, and screen reader interactions.
