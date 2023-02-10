import json
import time

from Gate.pageObjects.gateconsole import GateConsole
from Gateconsole_Adhoc_Arrival.pageObjects.livearrival import GateAdhocLiveArrival
from Login.pageObjects.login import LoginPage
from Utilis.readProperties import ReadConfig
from Configurations.conftest import set_up_tear_down

class LiveArrivalJSON:
    #Create static method
    @staticmethod
    def getlivearrivaljson():
        myjsonfile=open("C:/Users/VelKarthik/PycharmProjects/Playwright_YMS_2023/Gateconsole_Adhoc_Arrival/TestData/livearrival.json", "r")
        jsondata=myjsonfile.read()
        obj=json.loads(jsondata)
        formdetails = obj
        return obj

def test_gate_adhoc_livearrival(set_up_tear_down) -> None:
    page = set_up_tear_down
    credentials = {'emailaddress': ReadConfig.getUseremail(), 'password': ReadConfig.getPassword()}

    # Logged Successfully
    login_p = LoginPage(page)
    login_p.do_login(credentials)

    # Gate Console>> Gate and Site Selected
    gatecons = GateConsole(page)
    gatecons.gateconsole()

    # Arrival of Adhoc Drop Trailer
    gatela = GateAdhocLiveArrival(page)
    gatela.livearrival(LiveArrivalJSON.getlivearrivaljson())
    time.sleep(10)



