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

    def click_gate(self):    #Click on the Gate
        self._clickgate.click()

    def click_console(self):   #Click on the Console
        self._clickconsole.click()

    def select_siteandgate(self):   #Selection of Gate and Site
        self._selectsiteandgate.click()

    def choose_site(self):
        self._choosesite.click()

    def select_site(self):                #Site Seletion
        self._selectsite.click()

    def choose_gate(self):
        self._choosegate.click()

    def select_gate(self):                  #Gate Selection
        self._selectgate.click()

    def submit_onselection(self):            #Submit after Choosing the Site and Gate
        self._submitbutton.click(timeout=100)

    def gateconsole(self):
        self.click_gate()
        self.click_console()
        self.select_siteandgate()
        self.choose_site()
        self.select_site()
        self.choose_gate()
        self.select_gate()
        self.submit_onselection()




        # page.get_by_role("button", name="Gate ").click()
        # page.get_by_role("link", name="Console").click()
        # page.locator("a").filter(has_text="Select Site & Gate").click()
        # page.get_by_text("Choose Your Site").click()
        # page.get_by_text("collegedale").click()
        # page.get_by_text("Choose Your Gate").click()
        # page.get_by_text("P2_MAIN").click()
        # page.get_by_role("button", name="Submit").click()