## 2024-04-02 - Nested Interactive Elements in Download Buttons
**Learning:** Found a specific component pattern where <a> tags were nested inside <button> elements for downloads. This creates invalid HTML and breaks keyboard focus/screen reader accessibility.
**Action:** Replaced the nested elements with semantic <a> tags styled using CSS (.download-btn class with inline-block, hover/focus-visible states) to maintain visual appearance while ensuring full keyboard accessibility and valid HTML structure. Also updated paths to be relative and added the HTML5 download attribute for better UX.
