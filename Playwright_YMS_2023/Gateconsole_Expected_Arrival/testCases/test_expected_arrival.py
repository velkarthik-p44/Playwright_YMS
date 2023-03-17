import json
import time

from Gate.pageObjects.gateconsole import GateConsole
from Gateconsole_Expected_Arrival.pageObjects.expected_arrival import GateExpectedArrival
from Login.pageObjects.login import LoginPage
from Utilis.readProperties import ReadConfig
from Configurations.conftest import set_up_tear_down

class ExpectedArrivalJSON:
    #Create three static methods
    @staticmethod
    def getexpectedarrivaljson():
        myjsonfile=open("C:/Users/VelKarthik/PycharmProjects/Playwright_YMS_2023/Gateconsole_Expected_Arrival/TestData/expected_arrival.json", "r")
        jsondata=myjsonfile.read()
        obj=json.loads(jsondata)
        exparrival = obj
        return obj


def test_ship_dedtrailer_arrival(set_up_tear_down) -> None:
    page = set_up_tear_down
    credentials = {'emailaddress': ReadConfig.getUseremail(), 'password': ReadConfig.getPassword()}
    #Logged Successfully
    login_p = LoginPage(page)
    login_p.do_login(credentials)
    print("Logged in Successfully")

    # Gate Console>> Gate and Site Selected
    gatecons = GateConsole(page)
    gatecons.gateconsole()
    print("Redirected to Gate Console Screen")


    #Expected Arrival
    expectarrival = GateExpectedArrival(page)
    expectarrival.expectedarrival(ExpectedArrivalJSON.getexpectedarrivaljson())
    time.sleep(5)
    print("Expected Arrival")

