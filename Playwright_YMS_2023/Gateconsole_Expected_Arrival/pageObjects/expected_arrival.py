import string
from concurrent.futures import thread
import time

class GateExpectedArrival:

    def __init__(self, page):
        self.page = page
        #Click Expected
        self._clickexpected = page.get_by_text("Arrived Expected")
        #Input Values in the Search
        self._searchexpected = page.locator("(//input[@placeholder='Search'])[1]")
        #Enter Keypress
        self._enterkeypress = page.locator("(//input[@placeholder='Search'])[1]")
        #Select the First and Arrive
        self._clickarrive = page.locator("div:nth-child(1) > .info > .action > .new-button")
        #Enter Trailer#
        self._entertrail = page.locator("//input[@id='mat-input-1']")
        # Type Selection
        self._choosetype = page.get_by_text("Choose Type")
        self._selecttype = page.locator("form").get_by_title("TRAILER")

        # Seal 1 & 2
        self._enterseal1 = page.locator("#seal1_arrival")
        self._enterseal2 = page.locator("#seal2_arrival")

        # Cab Details
        self._entercab = page.locator("#cab_num_arrival")

        # Driver Details
        self._enterdrivercell = page.locator("#driver_cell_arrival")  # Cell Num
        self._enterfirstname = page.locator("#first_name")  # First Name
        self._enterlastname = page.locator("#last_name")  # Last Name
        self._enteremailid = page.locator("#driver_email_id")  # Email
        self._entercomments = page.locator("#comments_arrival")

        # Arrival Button
        self._actionarrival = page.get_by_role("button", name="Arrival")

        #Arrived Tab
        self._arrivedtab = page.get_by_text("Arrived")

    def click_expected(self):
        self._clickexpected.click()

    def search_expected(self, searchvalue):
        self._searchexpected.fill(searchvalue)

    def enter_keypress(self):
        self._enterkeypress.press("Enter")

    def click_arrive(self):
        self._clickarrive.click()

    def enter_trail(self, trai):
        self._entertrail.fill(trai)

    def choosetype(self):
        self._choosetype.click()

    def selecttype(self):
        self._selecttype.click()

    def enter_seal1(self, seal1):
        self._enterseal1.fill(seal1)

    def enter_seal2(self, seal2):
        self._enterseal2.fill(seal2)

    def enter_cab(self, cab):
        self._entercab.fill(cab)

    def enter_drivercell(self, cell):
        self._enterdrivercell.fill(cell)

    def enter_firstname(self, fname):
        self._enterfirstname.fill(fname)

    def enter_lastname(self, lname):
        self._enterlastname.fill(lname)

    def enter_emailid(self, emailid ):
        self._enteremailid.fill(emailid)

    def enter_comments(self, comments):
        self._entercomments.fill(comments)

    def exp_arrival(self):
        self._actionarrival.click()

    def arrived_tab(self):
        self._arrivedtab.click()


    def expectedarrival(self, exparrival):
        self.click_expected()
        self.search_expected(exparrival['Ship Num#'])
        self.enter_keypress()
        time.sleep(5)
        self.click_arrive()
        self.enter_trail(exparrival['Trailer#'])
        self.choosetype()
        self.selecttype()
        self.enter_seal1(exparrival['SEAL1'])
        self.enter_seal2(exparrival['SEAL2'])
        self.enter_cab(exparrival['CAB'])
        self.enter_drivercell(exparrival['DRIVER CELL'])
        self.enter_firstname(exparrival['FIRST NAME'])
        self.enter_lastname(exparrival['LAST NAME'])
        self.enter_emailid(exparrival['EMAIL'])
        self.enter_comments(exparrival['COMMENTS'])
        self.exp_arrival()
        self.arrived_tab()
