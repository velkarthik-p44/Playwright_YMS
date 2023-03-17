import string
from concurrent.futures import thread
import time

class TrailerListing:

    def __init__(self, page):
        self.page = page
        #Click Asset
        self._clickasset = page.locator("(//a[normalize-space()='Asset'])[1]")
        self._selecttrailerlist = page.locator("//a[normalize-space()='Trailer Listing']")
        #Input Values in the Search
        self._searchtrail = page.get_by_role("textbox", name="Search")
        self._enterkeypress = page.get_by_role("textbox", name="Search")

    def click_asset(self):
        self._clickasset.click()

    def select_tl(self):
        self._selecttrailerlist.click()

    def search_trail(self, trail):
        self._searchtrail.fill(trail)

    def enter_keypress(self):
        self._enterkeypress.press("Enter")

    def trailer_listing(self, traillist):
        self.click_asset()
        self.select_tl()
        self.search_trail(traillist['Trailer#'])
        time.sleep(5)
        self.enter_keypress()
        time.sleep(5)
