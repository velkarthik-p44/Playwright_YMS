from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError

class GateConsole:

    def __init__(self, page):
        self.page = page
        self._clickgate = page.get_by_role("button", name="Gate")
        self._clickconsole = page.get_by_role("link", name="Console")
        self._selectsiteandgate = page.locator("a").filter(has_text="Select Site & Gate")
        self._choosesite = page.get_by_text("Choose Your Site")
        self._selectsite = page.get_by_text("collegedale")
        self._choosegate = page.get_by_text("Choose Your Gate")
        self._selectgate = page.get_by_text("P2_MAIN")
        self._submitbutton = page.get_by_role("button", name="Submit")

    # Click on the Gate
    def click_gate(self):
        self._clickgate.click()

    # Click on the Console
    def click_console(self):
        self._clickconsole.click()

    # Selection of Gate and Site
    def select_siteandgate(self):
        self._selectsiteandgate.click()

    def choose_site(self):
        self._choosesite.click()

    # Site Seletion
    def select_site(self):
        self._selectsite.click()

    def choose_gate(self):
        self._choosegate.click()

    # Gate Selection
    def select_gate(self):
        self._selectgate.click()

    # Submit after Choosing the Site and Gate
    def submit_onselection(self):
        self._submitbutton.click()

    def gateconsole(self):
        self.click_gate()
        self.click_console()
        self.select_siteandgate()
        self.choose_site()
        self.select_site()
        self.choose_gate()
        self.select_gate()
        self.submit_onselection()

    def saved_gateconsole(self):
        self.click_gate()
        self.click_console()




