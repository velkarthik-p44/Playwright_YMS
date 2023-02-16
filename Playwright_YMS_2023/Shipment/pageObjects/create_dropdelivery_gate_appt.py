import time

from playwright.sync_api import expect

class CreateDropDeliveryAppt:

    def __init__(self, page):
        self.page = page
        self._clickshipment = page.get_by_text("Shipment")
        self._clickdelivery = page.get_by_text("Delivery")
        self._clickcreate = page.get_by_text("Create Delivery")
        self._entershipmentno = page.locator("#shipment_no")
        self._choosesite = page.get_by_text("Choose Site")
        self._selectsite = page.get_by_role("tabpanel", name="Details").get_by_text("collegedale")
        self._choosevendor = page.get_by_text("Choose Vendor")
        self._selectvendor = page.get_by_role("tabpanel", name="Details").get_by_text("mckee")
        self._choosecarrier = page.get_by_text("Choose Carrier")
        self._selectcarrier = page.get_by_text("abfs-abf")
        self._chooseloadtype = page.get_by_text("Choose Load Type")
        self._selectloadtype = page.get_by_role("tabpanel", name="Details").get_by_text("drop")
        self._enterreference1 = page.locator("#reference_1")
        self._enterreference2 = page.locator("#reference_2")
        self._entertrailer = page.locator("#trailer")
        self._enterlicenseplate = page.locator("#license_plate_no")
        self._nextpage1 = page.get_by_role("button", name="Next Step")
        self._nextpage2 = page.get_by_role("button", name="Next Step")
        #Add Schedule
        self._addschedule = page.get_by_role("button", name="Add Schedule")
        self._selectdate = page.locator("//i[@class='fas fa-angle-right']")
        self._selecttiming = page.locator("//span[normalize-space()='12:00']")
        self._confirmpop = page.locator("//span[normalize-space()='Confirm']")
        self._confirmschd = page.get_by_role("button", name="Confirm Schedule")

    def click_shipment(self):
        self._clickshipment.click()

    def select_delivery(self):
        self._clickdelivery.first.click()

    def create_delivery(self):
        self._clickcreate.click()

    def enter_shipment(self, num):
        self._entershipmentno.fill(num)

    def choose_site(self):
        self._choosesite.click()

    def select_site(self):
        self._selectsite.click()

    def choose_vendor(self):
        self._choosevendor.click()

    def select_vendor(self):
        self._selectvendor.click()

    def choose_carrier(self):
        self._choosecarrier.click()

    def select_carrier(self):
        self._selectcarrier.click()

    def choose_loadtype(self):
        self._chooseloadtype.click()

    def select_loadtype(self):
        self._selectloadtype.click()

    def enter_ref1(self, ref1):
        self._enterreference1.fill(ref1)

    def enter_ref2(self, ref2):
        self._enterreference2.fill(ref2)

    def enter_trailer(self, trailer):
        self._entertrailer.fill(trailer)

    def enter_lp(self, lp):
        self._enterlicenseplate.fill(lp)

    def next_page1(self):
        self._nextpage1.click()

    def next_page2(self):
        self._nextpage2.click()

    #Add Schedule
    def add_schedule(self):
        self._addschedule.click()

    def select_date(self):
        self._selectdate.click()
        time.sleep(5)

    def select_time(self):
        self._selecttiming.click()

    def confirm_pop(self):
        self._confirmpop.click()

    def confirm_schd(self):
        self._confirmschd.click()

    def newdropdeliveryappt(self, dropdeliveryappt):
        self.click_shipment()
        self.select_delivery()
        self.create_delivery()
        self.enter_shipment(dropdeliveryappt['Shipment#'])
        self.choose_site()
        self.select_site()
        self.choose_vendor()
        self.select_vendor()
        self.choose_carrier()
        self.select_carrier()
        self.choose_loadtype()
        self.select_loadtype()
        self.enter_ref1(dropdeliveryappt['Ref1'])
        self.enter_ref2(dropdeliveryappt['Ref2'])
        self.enter_trailer(dropdeliveryappt['Trailer'])
        self.enter_lp(dropdeliveryappt['LP'])
        self.next_page1()
        self.next_page2()
        # Add Schedule
        self.add_schedule()
        self.select_date()
        self.select_time()
        self.confirm_pop()
        self.confirm_schd()










