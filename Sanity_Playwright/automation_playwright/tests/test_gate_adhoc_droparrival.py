from Configurations.config import UserLogin
from automation_playwright.src.pages.Create_PickupPage import CreatePickupPage
from automation_playwright.src.pages.GateConsole import GateConsole
from automation_playwright.src.pages.Gate_Adhoc_DropArrival import GateAdhocDropArrival
from automation_playwright.src.pages.Gate_Adhoc_LiveArrival import GateAdhocLiveArrival
from automation_playwright.src.pages.LoginPage import LoginPage
import json
import time

from automation_playwright.tests import test_gate_adhoc_livearrival
class ReadJSON:
    #Create three static methods
    @staticmethod
    def getjsondata():
        myjsonfile=open("C:/Users/VelKarthik/PycharmProjects/Sanity_Playwright/testdata/gate_adhoc_droparrival.json", "r")
        jsondata=myjsonfile.read()
        obj=json.loads(jsondata)
        dropdetails = obj
        return obj

def test_gate_adhoc_droparrival(set_up_tear_down) -> None:
    page = set_up_tear_down
    credentials = {'emailaddress': 'stagemckeee@yopmail.com', 'password': 'Admin@123'}
    # credentials = {'emailaddress': 'sandboxmckeee@yopmail.com', 'password': 'Admin@123'}
    # dropdetails = obj


    login_p = LoginPage(page)
    login_p.do_login(credentials)                         # Logged Successfully

    gatecons = GateConsole(page)
    gatecons.gateconsole()                                #Gate Console>> Gate and Site Selected
    # gatela = GateAdhocLiveArrival(page)
    # gatela.livearrival(formdetails)
    gateda = GateAdhocDropArrival(page)
    gateda.droparrival(ReadJSON.getjsondata())           # Arrival of Adhoc Drop Arrival Trailer
    # time.sleep(10)
    page.pause()

