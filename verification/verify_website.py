from playwright.sync_api import sync_playwright
import os

def run(playwright):
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()

    # Get absolute path to index.html
    cwd = os.getcwd()
    file_path = f"file://{cwd}/index.html"

    print(f"Navigating to: {file_path}")
    page.goto(file_path)

    # Take a full page screenshot
    screenshot_path = "verification/website_screenshot.png"
    page.screenshot(path=screenshot_path, full_page=True)
    print(f"Screenshot saved to {screenshot_path}")

    browser.close()

if __name__ == "__main__":
    with sync_playwright() as playwright:
        run(playwright)
