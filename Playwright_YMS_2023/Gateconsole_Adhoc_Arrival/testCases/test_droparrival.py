
import json
import time

from Gate.pageObjects.gateconsole import GateConsole
from Gateconsole_Adhoc_Arrival.pageObjects.droparrival import GateAdhocDropArrival
from Configurations.conftest import set_up_tear_down
from Login.pageObjects.login import LoginPage


class DropArrivalJSON:
    #Create three static methods
    @staticmethod
    def getdroparrivaljson():
        myjsonfile=open("C:/Users/VelKarthik/PycharmProjects/Playwright_YMS_2023/Gateconsole_Adhoc_Arrival/TestData/droparrival.json", "r")
        jsondata=myjsonfile.read()
        obj=json.loads(jsondata)
        dropdetails = obj
        return obj

def test_gate_adhoc_droparrival(set_up_tear_down) -> None:
    page = set_up_tear_down
    credentials = {'emailaddress': 'stagemckeee@yopmail.com', 'password': 'Admin@123'}
    # credentials = {'emailaddress': 'sandboxmckeee@yopmail.com', 'password': 'Admin@123'}
    # dropdetails = obj

    # Logged Successfully
    login_p = LoginPage(page)
    login_p.do_login(credentials)

    # Gate Console>> Gate and Site Selected
    gatecons = GateConsole(page)
    gatecons.gateconsole()

    # Arrival of Adhoc Drop Trailer
    gateda = GateAdhocDropArrival(page)
    gateda.droparrival(DropArrivalJSON.getdroparrivaljson())
    time.sleep(10)


