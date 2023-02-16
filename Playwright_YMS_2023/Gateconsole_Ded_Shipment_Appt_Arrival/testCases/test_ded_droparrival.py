import json
import time

from Gate.pageObjects.gateconsole import GateConsole
from Gateconsole_Ded_Shipment_Appt_Arrival.pageObjects.ded_droparrival import GateDedDropArrival
from Login.pageObjects.login import LoginPage
from Utilis.readProperties import ReadConfig
from Configurations.conftest import set_up_tear_down


class DedDropArrivalJSON:
    #Create three static methods
    @staticmethod
    def getdroparrivaljson():
        myjsonfile=open("C:/Users/VelKarthik/PycharmProjects/Playwright_YMS_2023/Gateconsole_Ded_Shipment_Appt_Arrival/TestData/ded_droparrival.json", "r")
        jsondata=myjsonfile.read()
        obj=json.loads(jsondata)
        deddroparrival = obj
        return obj

def test_gate_ded_droparrival(set_up_tear_down) -> None:
    page = set_up_tear_down
    credentials = {'emailaddress': ReadConfig.getUseremail(), 'password': ReadConfig.getPassword()}

    # Logged Successfully
    login_p = LoginPage(page)
    login_p.do_login(credentials)
    print("Logged IN")

    # Gate Console>> Gate and Site Selected
    gatecons = GateConsole(page)
    gatecons.gateconsole()
    print("Redirected to Gate Console Screen")

    #Arrival of Shipment with Appt- Dedicated Trailer
    dedarrival = GateDedDropArrival(page)
    dedarrival.deddroparrival(DedDropArrivalJSON.getdroparrivaljson())
    time.sleep(5)
    print("Arrival of Shipment with Appt- Dedicated Trailer")



