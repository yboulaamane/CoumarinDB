## 2025-02-17 - Button Nesting
**Learning:** The application used invalid HTML by nesting <a> tags inside <button> elements for download links, which confuses screen readers and is semantically incorrect.
**Action:** Refactored to use styled <a> tags with role='button' (or just styled links) and proper aria-labels.
