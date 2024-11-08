from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://stackoverflow.com/questions/45927922/why-are-there-multiple-pip-versions-in-my-python-scripts-folder")
    print(page.title())
    page.wait_for_timeout(3000)
    browser.close()


