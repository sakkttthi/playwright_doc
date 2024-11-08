from playwright.sync_api import sync_playwright

# xpath & shadow root = closed, we cannot perform actions on shadow dom

with sync_playwright() as sy:
    browser = sy.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://selectorshub.com/xpath-practice-page/")

    # page.locator("#kils").fill("This is shadow") - exeption is thrown 

# Locate parent & then locate shadow element in it 
    parent_root = page.locator(".jackPart")
    parent_root.locator("#kils").fill("raju sign")
    page.wait_for_timeout(3000)