## 2024-05-27 - Fix Invalid Button/Link Nesting
**Learning:** Putting `<a>` tags inside `<button>` tags is an invalid pattern found in this app that breaks keyboard navigation and confuses screen readers. This app used this to trigger downloads.
**Action:** When a link that looks like a button is needed, use an `<a>` tag with the `download` attribute and style it with CSS to look like a button.
