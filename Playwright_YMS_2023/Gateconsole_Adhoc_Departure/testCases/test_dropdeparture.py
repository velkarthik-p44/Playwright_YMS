import json
import time

from Gate.pageObjects.gateconsole import GateConsole
from Gateconsole_Adhoc_Departure.pageObjects.dropdeparture import Gate_Adhoc_Drop_Departure
from Login.pageObjects.login import LoginPage
from Utilis.readProperties import ReadConfig
from Configurations.conftest import set_up_tear_down


class DropDepartureJSON:
    #Create static method
    @staticmethod
    def getdropdeparturejson():
        myjsonfile=open("C:/Users/VelKarthik/PycharmProjects/Playwright_YMS_2023/Gateconsole_Adhoc_Departure/TestData/dropdeparture.json", "r")
        jsondata=myjsonfile.read()
        obj=json.loads(jsondata)
        dropdepartdetails = obj
        return obj

def test_drop_departure(set_up_tear_down) -> None:
    page = set_up_tear_down
    #Login
    credentials = {'emailaddress': ReadConfig.getUseremail(), 'password': ReadConfig.getPassword()}
    login_p = LoginPage(page)
    login_p.do_login(credentials)
    #Gate Console
    gatecons = GateConsole(page)
    gatecons.gateconsole()
    #Adhoc Drop Departure
    dddepart = Gate_Adhoc_Drop_Departure(page)
    dddepart.gate_drop_departure(DropDepartureJSON.getdropdeparturejson())
    time.sleep(10)