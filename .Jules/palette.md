## 2026-09-29 - Screen reader announcements for temporary states
**Learning:** When a button temporarily changes text to provide feedback (like a 'Copied' state), screen readers don't announce it unless the button has aria-live attributes.
**Action:** Add aria-live="polite" to buttons that have temporary text flashes so the feedback is announced to screen readers.
