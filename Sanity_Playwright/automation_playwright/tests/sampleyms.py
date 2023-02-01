from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chrome.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://yard-visibility-na12.voc.qa-stage.p-44.com/")
    page.goto("https://yard-visibility-na12.voc.qa-stage.p-44.com/auth/login")
    page.get_by_label("Email Address").click()
    page.get_by_label("Email Address").fill("stagemckeee@yopmail.com")
    page.get_by_label("Password").click()
    page.get_by_label("Password").fill("Admin@123")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="Shipment ").click()
    page.get_by_role("link", name="Pickup").first.click()
    page.get_by_role("button", name="Create Pickup").click()
    page.locator("#shipment_no").click()
    page.locator("#shipment_no").fill("VKKK1")
    page.get_by_text("Choose Site").click()
    page.get_by_text("gentry").click()
    page.get_by_text("Choose Customer").click()
    page.get_by_role("tabpanel", name="Details").get_by_text("mckee").click()
    page.get_by_text("Choose Carrier").click()
    page.get_by_text("abfs-abf").click()
    page.get_by_text("Choose Load Type").click()
    page.get_by_role("tabpanel", name="Details").get_by_text("drop").click()
    page.get_by_role("button", name="Next Step").click()
    page.get_by_role("button", name="Next Step").click()

    page.get_by_role("button", name="Save Pickup").click()


    # ---------------------



with sync_playwright() as playwright:
    run(playwright)
