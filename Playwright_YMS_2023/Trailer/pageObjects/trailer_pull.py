import string
from concurrent.futures import thread
import time

class TrailerPull:
    def __init__(self, page):
        self.page = page
        #Create Pull
        self._clickpull = page.locator("//i[@class='icons fas fa-arrow-right ml-1']")
        self._roundtrip = page.get_by_text("?")
        self._turnofftoggle = page.locator("//label[normalize-space()='Yes']")
        # self._clickcondition = page.locator("//span[@title='Choose Condition']")
        # self._selectcondition = page.locator("//div[@class='multiselect-item-text']")
        self._clickcommodity = page.locator("(//span[@class='dropdown-multiselect__caret'])[14]")
        self._selectcommodity = page.locator("(//div[@class='form-group column m-0'])[3]//div")
        self._visibletext = page.get_by_label("Assigned To Driver")

        self._toogledriver = page.locator("//input[@id='auto_assign']")
        self._clickdriver = page.locator("//sui-select[@name='driver']")
        self._selectdriver = page.locator("//div[@class='assets']")

        self._createpull = page.get_by_role("button", name="Pull")

        self._confirmpull = page.locator("//i[@class='icons fas fa-arrow-right ml-1']")
        self._start = page.locator("//button[normalize-space()='Start']")
        self._confirmstart = page.locator("//span[normalize-space()='Start']")

        self._hook = page.locator("//button[normalize-space()='Hook']")
        self._confirmhook = page.locator("//span[normalize-space()='Hook']")

        self._complete = page.locator("//button[normalize-space()='Complete']")
        self._confirmcomplete = page.locator("//span[normalize-space()='Complete']")

        self._closepopup = page.locator("(//span[@class='close float-right'][contains(text(),'✕')])[2]")


    def click_pull(self):
        self._clickpull.nth(0).click()

    def turnoff_roundtrip(self):
        self._turnofftoggle.click()

    # def click_condition(self):
    #     self._clickcondition.click()
    #
    # def select_condition(self):
    #     self._selectcondition.nth(2).click()

    def click_commodity(self):
        self._clickcommodity.click()

    def select_commodity(self):
        self._selectcommodity.nth(2).click()

    # Enable the Auto Assign to Driver
    def toggle_assigndriver(self):
        self._toogledriver.click()


     # Click the Driver List
    def click_driver(self):
        self._clickdriver.click()

    def choose_driver(self):
        self._selectdriver.nth(1).click()

    def create_pull(self):
        self._createpull.click()

        # Initialize Pull task
    def confirm_pull(self):
        self._confirmpull.nth(0).click()

        # Start the Task
    def start( self ):
        self._start.click()

    def confirm_start(self):
        self._confirmstart.click()

        # Hook the Task
    def hook(self):
        self._hook.click()

    def confirm_hook(self):
        self._confirmhook.click()

    # Complete the Task
    def complete(self):
        self._complete.click()

    def confirm_complete(self):
        self._confirmcomplete.click()

    # Close the Pull Popup
    def close_popup(self):
        self._closepopup.click()

    def pulltrailer(self):
        self.click_pull()
        if self._roundtrip.is_visible():
            self.turnoff_roundtrip()
            # self.click_commodity()
            # self.select_commodity()
            print("Round Trip Available")
        else:
            # self.click_commodity()
            # self.select_commodity()
            print("Round Trip Option Not Available")

        self.click_commodity()
        self.select_commodity()

        if self._visibletext.is_visible():
            self.toggle_assigndriver()
            self.click_driver()
            self.choose_driver()
            self.create_pull()
        else:
            self.create_pull()
        self.confirm_pull()

        if self._start.is_visible():
            self.start()
            self.confirm_start()
            self.hook()
            self.confirm_hook()
            self.complete()
            self.confirm_complete()
        else:
            self.hook()
            self.confirm_hook()
            self.complete()
            self.confirm_complete()

        self.close_popup()


