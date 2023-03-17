import random
import string
from concurrent.futures import thread

class GateAdhocDropArrival:

    def __init__(self, page):
        self.page = page
        self._clickdrop = page.get_by_role("button", name="Drop")

        #Shipment Num
        self._clickshipment = page.locator("#mat-input-0")
        self._entershipmentnum = page.locator("#mat-input-0")

        #Trailer Number
        self._clicktrailer = page.locator("#mat-input-1")
        self._entertrailernum = page.locator("#mat-input-1")

        #Carrier Selection
        self._choosescac = page.get_by_text("Choose Carrier")
        self._seletscac = page.get_by_text("abfs-abf")

        #Type Selection
        self._choosetype = page.get_by_text("Choose Type")
        self._selecttype = page.locator("form").get_by_title("TRAILER")

        #Seal 1 & 2
        self._clickseal1 =  page.locator("#seal1_arrival")
        self._enterseal1 = page.locator("#seal1_arrival")
        self._clickseal2 = page.locator("#seal2_arrival")
        self._enterseal2 = page.locator("#seal2_arrival")

        #Cab Details
        self._clickcab= page.locator("#cab_num_arrival")
        self._entercab = page.locator("#cab_num_arrival")

        #Driver Details
        self._clickdrivercell = page.locator("#driver_cell_arrival")
        self._enterdrivercell = page.locator("#driver_cell_arrival")               #Cell Num
        self._clickfirstname = page.locator("#first_name")
        self._enterfirstname =page.locator("#first_name")                           #First Name
        self._clicklastname = page.locator("#last_name")
        self._enterlastname = page.locator("#last_name")                            #Last Name
        self._clickemailid = page.locator("#driver_email_id")
        self._enteremailid = page.locator("#driver_email_id")                           #Email
        # self._clickdriverlicense = page.locator("#driver_license_arrival")
        # self._enterdriverlicense = page.locator("#driver_license_arrival")
        # self._clicklicensestate = page.locator("#driver_license_state_arrival")
        # self._enterlicensestate = page.locator("#driver_license_state_arrival")
        self._clickcomments = page.locator("#comments_arrival")
        self._entercomments = page.locator("#comments_arrival")

        #Arrival Button
        self._actionarrival = page.get_by_role("button", name="Arrival")



    def click_drop(self):
        self._clickdrop.click()

    def click_shipmentnum(self):
        self._clickshipment.click()

    def enter_shipmentnum(self, snum):
        self._entershipmentnum.fill(snum)

    def click_trailernum(self):
        self._clicktrailer.click()

    def enter_trailernum(self, tnum):
        self._entertrailernum.fill(tnum)

    def choose_scac(self):
        self._choosescac.click()

    def select_scac(self):
        self._seletscac.click()

    def choosetype(self):
        self._choosetype.click()

    def selecttype(self):
        self._selecttype.click()

    def click_seal1(self):
        self._clickseal1.click()

    def enter_seal1(self, seal1):
        self._enterseal1.fill(seal1)

    def click_seal2(self):
        self._clickseal2.click()

    def enter_seal2(self, seal2):
        self._enterseal2.fill(seal2)

    def click_cab(self):
        self._clickcab.click()

    def enter_cab(self, cab):
        self._entercab.fill(cab)

    def click_drivercell(self):
        self._clickdrivercell.click()

    def enter_drivercell(self, cell):
        self._enterdrivercell.fill(cell)

    def click_firstname(self):
        self._clickfirstname.click()

    def enter_firstname(self, fname):
        self._enterfirstname.fill(fname)

    def click_lastname(self):
        self._clicklastname.click()

    def enter_lastname(self, lname):
        self._enterlastname.fill(lname)

    def click_emailid(self):
        self._clickemailid.click()

    def enter_emailid(self, emailid):
        self._enteremailid.fill(emailid)

    # def click_driverlicense(self):
    #     self.click_driverlicense().click()
    #
    # def enter_driverlicense(self, dlicense):
    #     self._enterdriverlicense.fill(dlicense)
    #
    # def click_licensestate(self):
    #     self._clicklicensestate.click()
    #
    # def enter_licensestate(self, lstate):
    #     self._enterlicensestate.fill(lstate)

    def click_comments(self):
        self._clickcomments.click()

    def enter_comments(self, comments):
        self._entercomments.fill(comments)

    def live_arrival(self):
        self._actionarrival.click()




    def droparrival(self, dropdetails):
        self.click_drop()
        self.click_shipmentnum()
        self.enter_shipmentnum(dropdetails['Shipment Num#'])
        self.click_trailernum()
        self.enter_trailernum(dropdetails['Trailer Num#'])
        self.choose_scac()
        self.select_scac()
        self.choosetype()
        self.selecttype()
        self.click_seal1()
        self.enter_seal1(dropdetails['SEAL1'])
        self.click_seal2()
        self.enter_seal2(dropdetails['SEAL2'])
        self.click_cab()
        self.enter_cab(dropdetails['CAB'])
        self.click_drivercell()
        self.enter_drivercell(dropdetails['DRIVER CELL'])
        self.click_firstname()
        self.enter_firstname(dropdetails['FIRST NAME'])
        self.click_lastname()
        self.enter_lastname(dropdetails['LAST NAME'])
        self.click_emailid()
        self.enter_emailid(dropdetails['EMAIL'])
        # self.click_driverlicense()
        # self.enter_driverlicense(dropdetails['DRIVER LICENSE'])
        # self.click_licensestate()
        # self.enter_licensestate(dropdetails['LICENSE STATE'])
        self.click_comments()
        self.enter_comments(dropdetails['COMMENTS'])
        self.live_arrival()


    # def random_generator( size=8, chars=string.ascii_uppercase + string.digits):
    #     return ''.join(random.choice(chars) for x in range(size))
