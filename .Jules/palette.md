## 2026-05-29 - Accessible Interactive Elements

**Learning:** Nesting interactive elements, such as placing an `<a>` inside a `<button>`, is a severe accessibility anti-pattern. This results in invalid HTML that creates significant confusion for screen readers, which struggle to determine the correct interactive context.

**Action:** Whenever a link needs to look like a button for visual consistency, implement it as a semantic `<a>` tag with appropriate CSS classes, `role="button"`, and descriptive `aria-label` attributes. Do not nest it inside a `<button>` tag. Ensure that appropriate hover, focus, and focus-visible outlines are included to maintain strong keyboard accessibility.
