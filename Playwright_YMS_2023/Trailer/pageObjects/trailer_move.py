import string
from concurrent.futures import thread
import time

class TrailerMove:
    def __init__(self, page):
        self.page = page
        #Create Spot
        self._clickmove = page.locator("(//i[@class='icons fas fa-arrow-right ml-1'])[1]")
        self._clickloc = page.locator("//div[@class='placeholder ng-star-inserted']")
        self._selectloc = page.locator("//div[@class='dropdown-content ng-trigger ng-trigger-dropdownAnimation']//span")
        self._visibletext = page.get_by_label("Assigned To Driver")
        self._toggledriver = page.locator("//input[@id='auto_assign']")
        self._clickdriver = page.locator("//sui-select[@name='driver']")
        self._selectdriver = page.locator("//div[@class='assets']")
        self._createmove = page.get_by_role("button", name="Move")



        self._confirmmove = page.locator("(//i[@class='icons fas fa-arrow-right ml-1'])[1]")
        self._start = page.locator("//button[normalize-space()='Start']")
        self._confirmstart = page.locator("//span[normalize-space()='Start']")

        self._hook = page.locator("//button[normalize-space()='Hook']")
        self._confirmhook = page.locator("//span[normalize-space()='Hook']")

        self._complete = page.locator("//button[normalize-space()='Complete']")
        self._confirmcomplete = page.locator("//span[normalize-space()='Complete']")

        self._closepopup = page.locator("(//span[@class='close float-right'][contains(text(),'✕')])[2]")


    def click_move(self):
        self._clickmove.nth(0).click()

    #Click Location Options
    def click_loc(self):
        self._clickloc.click()

    # Select the Location from List
    def select_loc(self):
        self._selectloc.nth(8).click()

    # Enable the Auto Assign to Driver
    def toggle_driver(self):
        self._toggledriver.click()


    #Click the Driver List
    def click_driver(self):
        self._clickdriver.click()

    #Select the Driver from List
    def select_driver(self):
        self._selectdriver.nth(1).click()

    #Click the Move Button
    def create_move(self):
        self._createmove.click()

    # Initialize Move task
    def confirm_move(self):
        self._confirmmove.nth(0).click()

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

    #Close the Move Popup
    def close_popup(self):
        self._closepopup.click()



    def movetrailer(self):
        self.click_move()
        self.click_loc()
        self.select_loc()
        if self._visibletext.is_visible():
            self.toggle_driver()
            self.click_driver()
            self.select_driver()
            self.create_move()
        else:
            self.create_move()

        self.confirm_move()

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


