## 2024-12-04 - Semantic interactive elements mapping

**Learning:** This repository used an accessibility anti-pattern where a semantic interactive element `<a>` was nested within another interactive element `<button>`. This results in poor behavior with screen readers and invalid HTML.
**Action:** Replaced the nesting with a single `<a>` tag stylized to look like a button via CSS, and applied `role="button"` and a descriptive `aria-label` to ensure both proper styling and keyboard/screen reader accessibility.
