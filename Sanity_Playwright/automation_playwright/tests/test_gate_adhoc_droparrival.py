from Configurations.config import UserLogin
from automation_playwright.src.pages.Create_PickupPage import CreatePickupPage
from automation_playwright.src.pages.GateConsole import GateConsole
from automation_playwright.src.pages.Gate_Adhoc_DropArrival import GateAdhocDropArrival
from automation_playwright.src.pages.Gate_Adhoc_LiveArrival import GateAdhocLiveArrival
from automation_playwright.src.pages.LoginPage import LoginPage
import json
import time

from automation_playwright.tests import test_gate_adhoc_livearrival

myjsonfile=open("C:/Users/VelKarthik/PycharmProjects/Sanity_Playwright/testdata/gate_adhoc_droparrival.json", "r")
jsondata=myjsonfile.read()

obj=json.loads(jsondata)

def test_gate_adhoc_droparrival(set_up_tear_down) -> None:
    page = set_up_tear_down
    credentials = {'emailaddress': 'stagemckeee@yopmail.com', 'password': 'Admin@123'}
    dropdetails = obj


    login_p = LoginPage(page)
    login_p.do_login(credentials)
    gatecons = GateConsole(page)
    gatecons.gateconsole()
    # gatela = GateAdhocLiveArrival(page)
    # test_gate_adhoc_livearrival.sample(page)
    gatela = GateAdhocDropArrival(page)
    gatela.droparrival(dropdetails)
    time.sleep(1)

