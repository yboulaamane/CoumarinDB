import os
from playwright.sync_api import sync_playwright

def verify():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # We need to intercept external resources as the sandbox might have restricted network
        page.route("**/*", lambda route: route.continue_() if "localhost" in route.request.url or "127.0.0.1" in route.request.url or route.request.url.startswith("file:") else route.abort())

        filepath = "file://" + os.path.abspath("index.html")
        page.goto(filepath, wait_until="commit")

        # Verify the alt text on the image
        img_alt = page.locator("img").first.get_attribute("alt")
        assert img_alt == "CoumarinDB Header", f"Expected alt='CoumarinDB Header', got '{img_alt}'"
        print(f"✅ Image alt text is '{img_alt}'")

        # Verify the download buttons
        buttons = page.locator(".download-btn")
        count = buttons.count()
        assert count == 3, f"Expected 3 download buttons, found {count}"
        print(f"✅ Found {count} download buttons with class .download-btn")

        for i in range(count):
            btn = buttons.nth(i)
            # Verify it's an 'a' tag
            tag_name = btn.evaluate("node => node.tagName.toLowerCase()")
            assert tag_name == "a", f"Expected button {i} to be 'a' tag, was '{tag_name}'"

            # Verify the download attribute exists
            has_download = btn.evaluate("node => node.hasAttribute('download')")
            assert has_download, f"Button {i} is missing 'download' attribute"

            href = btn.get_attribute("href")
            print(f"✅ Button {i} text: '{btn.inner_text()}', href: '{href}', download attribute present")

        print("All frontend verifications passed!")
        browser.close()

if __name__ == "__main__":
    verify()
