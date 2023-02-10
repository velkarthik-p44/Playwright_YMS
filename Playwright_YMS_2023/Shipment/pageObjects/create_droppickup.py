from playwright.sync_api import expect

class CreateDropPickupPage:

    def __init__(self, page):
        self.page = page
        self._clickshipment = page.get_by_text("Shipment")
        self._clickpickup = page.get_by_text("Pickup")
        self._clickcreate = page.get_by_text("Create Pickup")
        self._clickshipmentno = page.locator("#shipment_no")
        self._entershipmentno = page.locator("#shipment_no")
        self._choosesite = page.get_by_text("Choose Site")
        self._selectsite = page.get_by_role("tabpanel", name="Details").get_by_text("collegedale")
        self._choosecustomer = page.get_by_text("Choose Customer")
        self._selectcustomer = page.get_by_text("pepsico")
        self._choosecarrier = page.get_by_text("Choose Carrier")
        self._selectcarrier = page.get_by_text("artd-a & r logistics/transport")
        self._chooseloadtype = page.get_by_text("Choose Load Type")
        self._selectloadtype = page.get_by_role("tabpanel", name="Details").get_by_text("drop")
        self._clickreference1 = page.locator("#reference_1")
        self._enterreference1 = page.locator("#reference_1")
        self._clickreference2 = page.locator("#reference_2")
        self._enterreference2 = page.locator("#reference_2")
        self._clicktrailer = page.locator("#trailer")
        self._entertrailer = page.locator("#trailer")
        self._clicklicenseplate = page.locator("#license_plate_no")
        self._enterlicenseplate = page.locator("#license_plate_no")
        self._nextpage1 = page.get_by_role("button", name="Next Step")
        self._nextpage2 = page.get_by_role("button", name="Next Step")
        self._savepickup = page.get_by_role("button", name="Save Pickup")

    def click_shipment(self):
        self._clickshipment.click()

    def select_pickup(self):
        self._clickpickup.first.click()

    def create_pickup(self):
        self._clickcreate.click()

    def click_pickup(self):
        self._clickshipmentno.click()

    def enter_shipment(self, num):
        self._entershipmentno.fill(num)

    def choose_site(self):
        self._choosesite.click()

    def select_site(self):
        self._selectsite.click()

    def choose_customer(self):
        self._choosecustomer.click()

    def select_customer(self):
        self._selectcustomer.click()

    def choose_carrier(self):
        self._choosecarrier.click()

    def select_carrier(self):
        self._selectcarrier.click()

    def choose_loadtype(self):
        self._chooseloadtype.click()

    def select_loadtype(self):
        self._selectloadtype.click()

    def click_ref1(self):
        self._clickreference1.click()

    def enter_ref1(self, ref1):
        self._enterreference1.fill(ref1)

    def click_ref2( self ):
        self._clickreference2.click()

    def enter_ref2(self, ref2):
        self._enterreference2.fill(ref2)

    def click_trailer(self, trailer):
        self._clicktrailer.click()

    def enter_trailer(self, trailer):
        self._entertrailer.fill(trailer)

    def click_lp(self, lp):
        self._clicklicenseplate.click()

    def enter_lp(self, lp):
        self._enterlicenseplate.fill(lp)

    def next_page1(self):
        self._nextpage1.click()

    def next_page2(self):
        self._nextpage2.click()


    def save_pickup(self):
        self._savepickup.click()

    def newdroppickup(self, droppickupdetails):
        self.click_shipment()
        self.select_pickup()
        self.create_pickup()
        self.click_pickup()
        self.enter_shipment(droppickupdetails['Shipment#'])
        self.choose_site()
        self.select_site()
        self.choose_customer()
        self.select_customer()
        self.choose_carrier()
        self.select_carrier()
        self.choose_loadtype()
        self.select_loadtype()
        self.enter_ref1(droppickupdetails['Ref1'])
        self.enter_ref2(droppickupdetails['Ref2'])
        self.enter_trailer(droppickupdetails['Trailer'])
        self.enter_lp(droppickupdetails['LP'])
        self.next_page1()
        self.next_page2()
        self.save_pickup()










