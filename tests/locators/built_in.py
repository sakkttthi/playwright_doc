'''
page.get_by_role() to locate by explicit and implicit accessibility attributes.
page.get_by_text() to locate by text content.
page.get_by_label() to locate a form control by associated label's text.
page.get_by_placeholder() to locate an input by placeholder.
page.get_by_alt_text() to locate an element, usually image, by its text alternative.
page.get_by_title() to locate an element by its title attribute.
page.get_by_test_id() to locate an element based on its data-testid attribute (other attributes can be configured).
'''
from playwright.sync_api import sync_playwright

with sync_playwright() as play:
    browser = play.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.tutorialspoint.com/selenium/practice/buttons.php")

# By role
# button, checkbox, menuitem, menuitemcheckbox, menuitemradio, option, radio, switch, tab or treeitem, link 
    page.get_by_role("button", name="Click Me", exact=True).click() #faced issue, locators had more reference so we user exact keyword to match

# By text 
    double_click = page.get_by_text("Double Click Me")
    double_click.dblclick()
    page.wait_for_timeout(3000)

# By placeholder
    page.goto("https://www.tutorialspoint.com/selenium/practice/text-box.php")
    placeholder_txt = page.get_by_placeholder("Full Name")
    placeholder_txt.fill("abc - ramu")
    page.wait_for_timeout(3000)

# By title
    page.goto("https://testautomationpractice.blogspot.com/")
    page.get_by_title("Automation Testing Practice")

# By test id - it is a cutom definition of locator used only for testing purpose, proposing this with dev
# playwright.selectors.set_test_id_attribute("data-pw") - to set test id of choice


# By label

# By alt txt 
