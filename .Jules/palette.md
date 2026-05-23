## 2024-05-23 - Interactive Element Nesting
**Learning:** Nesting interactive elements, such as placing an <a> tag inside a <button> tag, creates invalid HTML and severe accessibility issues. Screen readers and keyboard navigation struggle to interpret which action to trigger.
**Action:** Always use a single, semantic interactive element. For navigation links, use an <a> tag styled to look like a button rather than wrapping it inside an actual <button> element.
