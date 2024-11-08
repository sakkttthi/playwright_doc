from playwright.sync_api import sync_playwright

with sync_playwright() as play:
    browser = play.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://testautomationpractice.blogspot.com/")
  
# css selector #id, .class, tagname[attribute = 'value']
# To use css selector or xpath we should use page.locator()
    name = page.locator("#name")
    name.fill("Raju")

    email = page.locator("//input[@placeholder = 'Enter EMail']")
    email.fill("raju@g.com")

    page.wait_for_timeout(3000)