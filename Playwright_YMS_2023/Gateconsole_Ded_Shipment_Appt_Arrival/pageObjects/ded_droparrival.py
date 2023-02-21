import random
import string
from concurrent.futures import thread
import time

class GateDedDropArrival:

    def __init__(self, page):
        self.page = page
        self._clickdrop = page.get_by_role("button", name="Drop")

        #Shipment Num
        self._clickshipment = page.locator("#mat-input-0")
        self._entershipmentnum = page.locator("#mat-input-0")
        self._selectshipmentnum = page.locator("//span[@class='mat-option-text']").nth(0)

        #Trailer Number
        self._clicktrailer = page.locator("#mat-input-1")
        self._entertrailernum = page.locator("#mat-input-1")
        self._selecttrailernum = page.locator("//span[@class='mat-option-text']").nth(0)

        #Cab Details
        self._entercab = page.locator("#cab_num_arrival")

        #Driver Details
        self._enterdrivercell = page.locator("#driver_cell_arrival")               #Cell Num
        self._enterfirstname =page.locator("#first_name")                           #First Name
        self._enterlastname = page.locator("#last_name")                            #Last Name
        self._enteremailid = page.locator("#driver_email_id")                           #Email
        # self._clickdriverlicense = page.locator("#driver_license_arrival")
        # self._enterdriverlicense = page.locator("#driver_license_arrival")
        # self._clicklicensestate = page.locator("#driver_license_state_arrival")
        # self._enterlicensestate = page.locator("#driver_license_state_arrival")
        self._entercomments = page.locator("#comments_arrival")

        #Arrival Button
        self._actionddarrival = page.get_by_role("button", name="Arrival")


    def click_drop(self):
        self._clickdrop.click()

    def click_shipmentnum(self):
        self._clickshipment.click()

    def enter_shipmentnum(self, snum):
        self._entershipmentnum.fill(snum)

    def select_shipmentnum( self ):
        self._selectshipmentnum.click()

    def click_trailernum(self):
        self._clicktrailer.click()

    def enter_trailernum(self, tnum):
        self._entertrailernum.fill(tnum)

    def select_trailernum( self ):
        self._selecttrailernum.click()

    def enter_cab(self, cab):
        self._entercab.fill(cab)

    def enter_drivercell(self, cell):
        self._enterdrivercell.clear()
        self._enterdrivercell.fill(cell)

    def enter_firstname(self, fname):
        self._enterfirstname.clear()
        self._enterfirstname.fill(fname)

    def enter_lastname(self, lname):
        self._enterlastname.clear()
        self._enterlastname.fill(lname)

    def enter_emailid(self, emailid):
        self._enteremailid.clear()
        self._enteremailid.fill(emailid)

    def enter_comments(self, comments):
        self._entercomments.fill(comments)

    def dropded_arrival(self):
        self._actionddarrival.click()


    def deddroparrival(self, deddroparrival):
        self.click_drop()
        self.click_shipmentnum()
        self.enter_shipmentnum(deddroparrival['Shipment Num#'])
        time.sleep(10)
        self.select_shipmentnum()
        self.click_trailernum()
        self.enter_trailernum(deddroparrival['Trailer Num#'])
        time.sleep(10)
        self.select_trailernum()
        self.enter_cab(deddroparrival['CAB'])
        self.enter_drivercell(deddroparrival['DRIVER CELL'])
        self.enter_firstname(deddroparrival['FIRST NAME'])
        self.enter_lastname(deddroparrival['LAST NAME'])
        self.enter_emailid(deddroparrival['EMAIL'])
        self.enter_comments(deddroparrival['COMMENTS'])
        self.dropded_arrival()
        time.sleep(5)


    # def random_generator( size=8, chars=string.ascii_uppercase + string.digits):
    #     return ''.join(random.choice(chars) for x in range(size))
