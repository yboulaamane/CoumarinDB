## 2024-06-02 - Fixing nested interactive elements for better accessibility and UX

**Learning:** I encountered an HTML pattern where developers attempt to style links as buttons by nesting an anchor tag (`<a>`) inside a `<button>` tag (`<button><a>...</a></button>`). This is an invalid HTML pattern that creates nested interactive elements. It confuses screen readers (which element should they announce/interact with?) and leads to inconsistent focus behavior during keyboard navigation.

**Action:** In the future, I will fix this pattern by converting the element to a single semantic anchor tag styled as a button using CSS (`<a role="button" class="btn">`). I will ensure it has proper `aria-label`s if needed, `hover` styles for visual feedback, and a `focus-visible` outline for keyboard accessibility.
