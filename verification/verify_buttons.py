from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("http://localhost:8000/index.html")

        # Take a screenshot of the download section
        # Locate the element containing "Download:" and the buttons
        # We can try to grab the whole body or just the relevant area.
        # Let's target the buttons specifically.

        # Get the first button
        btn = page.locator('.download-btn').first

        # Scroll to it
        btn.scroll_into_view_if_needed()

        # Take screenshot
        page.screenshot(path="verification/buttons.png")

        browser.close()

if __name__ == "__main__":
    run()
