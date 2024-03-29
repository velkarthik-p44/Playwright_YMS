import time


class Gate_Adhoc_Live_Departure():

    def __init__(self, page):
        self.page = page
        self._clicknewdeparture = page.locator("//span[normalize-space()='New Departure']")
        self._ldtrailerlist = page.locator("//ml-select[contains(@name,'asset_type_arrival')]")
        self._entertrailernum = page.get_by_role("textbox", name="multiselect-search")
        self._selectentertrailernum = page.locator("//ml-select[@ng-reflect-placeholder='Trailer']//li").nth(2)
        self._confirmdepart = page.locator("#gate-console-departure").get_by_role("button", name="Depart")
        self._depart = page.get_by_role("button", name="Confirm")

    def click_newdeparture(self):
        self._clicknewdeparture.click()

    def click_ldtrailerlist(self):
        self._ldtrailerlist.click()

    def enter_trailernum(self, trailernum):
        self._entertrailernum.fill(trailernum)

    def select_trailernum(self):
        self._selectentertrailernum.click()

    def select_confirmdepart(self):
        self._confirmdepart.click()

    def depart(self):
        self._depart.click()

    def gate_live_departure(self, departdetails):
        self.click_newdeparture()
        self.click_ldtrailerlist()
        time.sleep(5)
        self.enter_trailernum(departdetails['TRAI#'])
        time.sleep(5)
        self.select_trailernum()
        self.select_confirmdepart()
        self.depart()















