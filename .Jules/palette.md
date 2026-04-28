## 2024-04-28 - Avoid nesting interactive elements
**Learning:** Nesting `<a>` inside `<button>` is invalid HTML and breaks keyboard accessibility and screen reader navigation, as standard interactive components should not contain other interactive components.
**Action:** When styled buttons simply act as links, replace the `<button>` wrapper with a semantic `<a>` tag. Apply CSS classes to retain the button-like appearance and ensure `display: inline-block` and focus/hover states are properly defined to restore the visual feedback normally provided by native buttons.
