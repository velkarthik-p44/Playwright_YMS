import string
from concurrent.futures import thread
import time

class TrailerSpot:
    def __init__(self, page):
        self.page = page
        #Create Spot
        self._clickspot = page.locator("//i[@class='icons fas fa-arrow-right']")
        self._clickdd = page.locator("//mdb-select[@name='location']")
        self._selectdd = page.locator("//mdb-select[@name='location']//li")
        self._visibletext = page.get_by_label("Assigned To Driver")
        self._toggledriver = page.locator("//input[@id='auto_assign']")
        self._clickdriver = page.locator("//sui-select[@name='driver']")
        self._selectdriver = page.locator("//div[@class='assets']")
        self._createspot = page.get_by_role("button", name="Spot")

        self._confirmspot = page.locator("//i[@class='icons fas fa-arrow-right']")
        self._start = page.locator("//button[normalize-space()='Start']")
        self._confirmstart = page.locator("//span[normalize-space()='Start']")

        self._hook = page.locator("//button[normalize-space()='Hook']")
        self._confirmhook = page.locator("//span[normalize-space()='Hook']")

        self._complete = page.locator("//button[normalize-space()='Complete']")
        self._confirmcomplete = page.locator("//span[normalize-space()='Complete']")

        self._closepopup = page.locator("(//span[@class='close float-right'][contains(text(),'✕')])[2]")


    def click_spot(self):
        self._clickspot.nth(0).click()

    #Click Dock Door Options
    def click_dd(self):
        self._clickdd.click()

    # Select the Dock Door from List
    def select_dd(self):
        self._selectdd.nth(0).click()

    # Enable the Auto Assign to Driver
    def toggle_driver(self):
        self._toggledriver.click()


    #Click the Driver List
    def click_driver(self):
        self._clickdriver.click()

    #Select the Driver from List
    def select_driver(self):
        self._selectdriver.nth(1).click()

    #Click the Spot Button
    def create_spot(self):
        self._createspot.click()

    # Initialize Spot task
    def confirm_spot(self):
        self._confirmspot.nth(0).click()

    # Start the Task
    def start(self):
        self._start.click()

    def confirm_start(self):
        self._confirmstart.click()

    # Hook the Task
    def hook(self):
        self._hook.click()

    def confirm_hook(self):
        self._confirmhook.click()

    #Complete the Task
    def complete(self):
        self._complete.click()

    def confirm_complete(self):
        self._confirmcomplete.click()

    #Close the Spot Popup
    def close_popup(self):
        self._closepopup.click()



    def spottrailer(self):
        self.click_spot()
        self.click_dd()
        self.select_dd()
        if self._visibletext.is_visible():
            self.toggle_driver()
            self.click_driver()
            self.select_driver()
            self.create_spot()
        else:
            self.create_spot()
        self.confirm_spot()

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


