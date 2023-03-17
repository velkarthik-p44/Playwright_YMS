import string
from concurrent.futures import thread
import time

class TrailerBump:
    def __init__(self, page):
        self.page = page
        #Create Spot
        self._clickbump = page.locator("(//i[@class='icons fas fa-arrow-up ml-1'])[1]")
        self._toggledriver = page.locator("//input[@id='auto_assign']")
        self._clickdriver = page.locator("//sui-select[@name='driver']")
        self._selectdriver = page.locator("//div[@class='assets']")
        self._createbump = page.get_by_role("button", name="Bump")

        self._confirmbump = page.locator("(//i[@class='icons fas fa-arrow-up ml-1'])[1]")
        self._start = page.locator("//button[normalize-space()='Start']")
        self._confirmstart = page.locator("//span[normalize-space()='Start']")

        self._hook = page.locator("//button[normalize-space()='Hook']")
        self._confirmhook = page.locator("//span[normalize-space()='Hook']")

        self._complete = page.locator("//button[normalize-space()='Complete']")
        self._confirmcomplete = page.locator("//span[normalize-space()='Complete']")

        self._closepopup = page.locator("(//span[@class='close float-right'][contains(text(),'✕')])[2]")


    def click_bump(self):
        self._clickbump.nth(0).click()

    # Enable the Auto Assign to Driver
    def toggle_driver(self):
        self._toggledriver.click()

    #Click the Driver List
    def click_driver(self):
        self._clickdriver.click()

    #Select the Driver from List
    def select_driver(self):
        self._selectdriver.nth(1).click()

    #Click the Bump Button
    def create_bump(self):
        self._createbump.click()

    # Initialize Bump task
    def confirm_bump(self):
        self._confirmbump.nth(0).click()

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

    #Close the Bump Popup
    def close_popup(self):
        self._closepopup.click()



    def bumptrailer(self):
        self.click_bump()
        self.toggle_driver()
        self.click_driver()
        self.select_driver()
        self.create_bump()
        self.confirm_bump()
        self.start()
        self.confirm_start()
        self.hook()
        self.confirm_hook()
        self.complete()
        self.confirm_complete()
        self.close_popup()


