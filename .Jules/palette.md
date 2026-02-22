## 2026-02-22 - Nested Interactive Elements in Action Buttons
**Learning:** Found <button> elements wrapping <a> tags for "Download" actions. This is invalid HTML and causes accessibility issues for screen readers and keyboard navigation.
**Action:** Replace with semantic <a> tags styled as buttons (.download-btn) using CSS. Ensure rel="noopener noreferrer" is added for target="_blank".
