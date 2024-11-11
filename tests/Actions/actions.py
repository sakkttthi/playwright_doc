from playwright.sync_api import sync_playwright, expect

with sync_playwright() as play:
    browser = play.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://testautomationpractice.blogspot.com/")

# Text input 
    name = page.get_by_placeholder("Enter Name")
    name.fill("Ramesh")

# Check box and radio button
    # male_radio = page.locator("#male")
    male_radio =  page.get_by_role("radio",name="Male",exact=True)
    male_radio.check()

    # page.locator("#monday").check()
    page.get_by_role("checkbox",name="Monday").check()

# Dropdown and select 
    dropdown = page.get_by_label("Country:")
    dropdown.select_option("Germany")

    select1 = page.get_by_label("Colors:")
    select1.select_option(value="green")

    # page.get_by_label('Choose multiple colors').select_option(['red', 'green', 'blue'])

# Mouse actions
# Click
    start_button = page.get_by_role("button",name="START")
    start_button.click()
    stop_button = page.get_by_role("button",name="STOP")
    expect(stop_button).to_have_text("STOP")

# Hover
    Hover_btn = page.get_by_role("button",name="Point Me")
    Hover_btn.hover()

# Double click
    dbl_btn = page.get_by_role("button",name="Copy Text")
    dbl_btn.dblclick()

    
# Drag & drop 
    pick = page.locator("#draggable")
    drop = page.locator("#droppable")
    pick.drag_to(drop)
    expect(drop, "Color doesnt change").to_have_css("background-color","rgc(255, 250, 144)")

# Shift + click
    # page.get_by_text("Item").click(modifiers=["Shift"])

# Click the top left corner
    # page.get_by_text("Item").click(position={ "x": 0, "y": 0})

# Type characters in field 
    page.locator("#email").press_sequentially("abc@gmail.com")

# Keyboard actions
    # Hit Enter
    # page.get_by_text("Submit").press("Enter")

# Dispatch Control+Right
    # page.get_by_role("textbox").press("Control+ArrowRight")

# Press $ sign on keyboard
    # page.get_by_role("textbox").press("$")


# Backquote, Minus, Equal, Backslash, Backspace, Tab, Delete, Escape,
# ArrowDown, End, Enter, Home, Insert, PageDown, PageUp, ArrowRight,
# ArrowUp, F1 - F12, Digit0 - Digit9, KeyA - KeyZ, etc.
 

# Upload files 
    page.locator("#singleFileInput").set_input_files("Files_to_upload\sample_to_upload_one.txt")
    page.locator("#multipleFilesInput").set_input_files(["Files_to_upload\sample_to_upload_one.txt","Files_to_upload\sample_to_upload_two.txt"])

# Scroll - automactically scrolls to interact with element 
    page.locator("#multipleFilesInput").scroll_into_view_if_needed()
    # page.mouse.wheel(0, 10) - location scroll

# Focus
    page.get_by_placeholder("Enter Phone").focus()

    page.wait_for_timeout(3000)
    
    
