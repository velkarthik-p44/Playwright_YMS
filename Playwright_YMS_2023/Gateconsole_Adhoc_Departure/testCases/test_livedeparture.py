import json
import time

from Gate.pageObjects.gateconsole import GateConsole
from Gateconsole_Adhoc_Departure.pageObjects.livedeparture import Gate_Adhoc_Live_Departure
from Login.pageObjects.login import LoginPage
from Utilis.readProperties import ReadConfig
from Configurations.conftest import set_up_tear_down


class LiveDepartureJSON:
    #Create static method
    @staticmethod
    def getlivedeparturejson():
        myjsonfile=open("C:/Users/VelKarthik/PycharmProjects/Playwright_YMS_2023/Gateconsole_Adhoc_Departure/TestData/livedeparture.json", "r")
        jsondata=myjsonfile.read()
        obj=json.loads(jsondata)
        values = obj
        return obj

def test_live_departure(set_up_tear_down) -> None:
    page = set_up_tear_down
    #Login
    credentials = {'emailaddress': ReadConfig.getUseremail(), 'password': ReadConfig.getPassword()}
    login_p = LoginPage(page)
    login_p.do_login(credentials)
    print("Logged In Successfully")

    #Gate Console
    gatecons = GateConsole(page)
    gatecons.gateconsole()
    print("Gate Console-Success")

    #Adhoc Live Departure
    lvdepart = Gate_Adhoc_Live_Departure(page)
    lvdepart.gate_live_departure(LiveDepartureJSON.getlivedeparturejson())
    print("Trailer - Departure")

    time.sleep(10)