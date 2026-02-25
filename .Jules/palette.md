## 2025-02-18 - Fix Invalid Button Nesting
**Learning:** Developers often nest anchor tags inside button tags to achieve a clickable appearance, but this is invalid HTML that disrupts accessibility tools and keyboard navigation.
**Action:** When encountering nested interactive elements, refactor them into a single valid element (e.g., styled anchor tag) and ensure CSS maintains the original visual design.
