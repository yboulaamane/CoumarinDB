## 2024-04-30 - Fix Interactive Element Nesting
**Learning:** Native `<button>` elements containing nested `<a>` links create invalid HTML and severe keyboard navigation/screen reader accessibility issues. They trap focus and confuse user intent.
**Action:** Always replace `button > a` nested elements with semantic `<a class="...">` tags styled as buttons. Provide explicit `:hover` and `:focus-visible` pseudo-classes using `display: inline-block` to preserve interactive visual feedback.
