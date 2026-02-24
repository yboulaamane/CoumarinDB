## 2024-05-22 - Nested Interactive Elements Pattern
**Learning:** Found a pattern of nesting `<a>` tags inside `<button>` tags for download links. This creates invalid HTML and accessibility barriers as screen readers may announce "button" but the action is navigation.
**Action:** Replace nested interactive elements with the semantically correct element (in this case, `<a>` styled as a button) to ensure proper accessibility and valid HTML.
