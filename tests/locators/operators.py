from playwright.sync_api import sync_playwright

with sync_playwright() as sy:
    browser = sy.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("")


# Below listed are mock only

# Macthing locator - 1
product = page.get_by_role("listitem").filter(has_text="Product 2")
product.get_by_role("button", name="Add to cart").click() #Here locator is written upon another locator

# Macthing locator - 2
save_button = page.get_by_role("button", name="Save")
dialog = page.get_by_test_id("settings-dialog")
dialog.locator(save_button).click() #Here test id is linked with button having "save" as text

# Matching two locators simultaneously (.and_)
button = page.get_by_role("button").and_(page.getByTitle("Subscribe"))

# Matching one of the two alternative locators(.or_)
button = page.get_by_role("button").or_(page.getByTitle("Subscribe"))

# Matching only visible elements
'''
<button style='display: none'>Invisible</button>
<button>Visible</button>
'''
# In above case use visible = true to avoid error 
page.locator("button").locator("visible=true").click()

