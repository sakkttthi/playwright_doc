from playwright.sync_api import sync_playwright
'''
<ul>
  <li>
    <h3>Product 1</h3>
    <button>Add to cart</button>
  </li>
  <li>
    <h3>Product 2</h3>
    <button>Add to cart</button>
  </li>
</ul>
'''

with sync_playwright() as sy:
    browser = sy.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("")

# Below listed are mock only
# Filter by text
    page.get_by_role("listitem").filter(has_text="Product 2").get_by_role("button",name="Add to cart")

# Filter by not having text
    page.get_by_role("listitem").filter(has_not_text=="Product 3").get_by_role("button",name="Add to cart")

# Filter by child/descendant
    page.get_by_role("listitem").filter(has=page.get_by_role("heading",name="Product 2").get_by_role("button",name="Add to cart"))

# Filter not by child/descendant
    page.get_by_role("listitem").filter(has_not==page.get_by_role("heading",name="Product 2").get_by_role("button",name="Add to cart"))
