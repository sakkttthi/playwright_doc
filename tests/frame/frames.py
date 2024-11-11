from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.hyrtutorials.com/p/frames-practice.html")

# Using any locator to locate frames
    frame2 = page.frame_locator("#frm2") 

# Using iframe tag url to locate 
    frame2 = page.frame(url="https://www.hyrtutorials.com/p/basic-controls.html")
    frame2_fname = frame2.get_by_placeholder("Enter First Name")
    frame2_fname.fill("Ramu")

    frame2_fname.scroll_into_view_if_needed()
    page.wait_for_timeout(3000)