import json
import time
from Gate.pageObjects.gateconsole import GateConsole
from Gateconsole_Adhoc_Arrival.pageObjects.drophookarrival import GateAdhocDropHook
from Gateconsole_Adhoc_Arrival.pageObjects.livearrival import GateAdhocLiveArrival
from Login.pageObjects.login import LoginPage
from Configurations.conftest import set_up_tear_down
from Utilis.readProperties import ReadConfig


class DropHookJSON:
    #Create static method
    @staticmethod
    def getdrophookjson():
        myjsonfile=open("C:/Users/VelKarthik/PycharmProjects/Playwright_YMS_2023/Gateconsole_Adhoc_Arrival/TestData/drophookarrival.json", "r")
        jsondata=myjsonfile.read()
        obj=json.loads(jsondata)
        drophookdetails = obj
        return obj

def test_gate_adhoc_drophook(set_up_tear_down) -> None:
    page = set_up_tear_down
    credentials = {'emailaddress': ReadConfig.getUseremail(), 'password': ReadConfig.getPassword()}

    # Logged Successfully
    login_p = LoginPage(page)
    login_p.do_login(credentials)

    # Gate Console>> Gate and Site Selected
    gatecons = GateConsole(page)
    gatecons.gateconsole()

    # Arrival of Adhoc Drop Hook Trailer(Empty Pickup)
    gatela = GateAdhocLiveArrival(page)
    gatedh = GateAdhocDropHook(page)
    gatedh.drophookarrival(DropHookJSON.getdrophookjson())
    time.sleep(10)
    # page.pause()

