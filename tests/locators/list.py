from playwright.sync_api import sync_playwright

with sync_playwright() as sy:
    browser = sy.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("")
    
'''
<ul>
  <li>apple</li>
  <li>banana</li>
  <li>orange</li>
</ul>
'''

page.get_by_role("listitem").to_have_count(3)
page.get_by_role("listitem").to_have_text(["apple", "banana", "orange"])
# Get by text
page.get_by_text("orange").click()
# filter by text
page.get_by_role("listitem").filter(has_text="orange").click()
# By item location
banana = page.get_by_role("listitem").nth(1)