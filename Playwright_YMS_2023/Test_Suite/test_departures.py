#Contain Test Case for Adhoc/Non-Dedicated Trailer Departures
#Includes Live, Drop and Drop Hook

import json
import time

from Gate.pageObjects.gateconsole import GateConsole
from Gateconsole_Adhoc_Departure.pageObjects.dropdeparture import Gate_Adhoc_Drop_Departure
from Gateconsole_Adhoc_Departure.pageObjects.livedeparture import Gate_Adhoc_Live_Departure
from Gateconsole_Adhoc_Departure.testCases.test_dropdeparture import DropDepartureJSON
from Gateconsole_Adhoc_Departure.testCases.test_livedeparture import LiveDepartureJSON
from Login.pageObjects.login import LoginPage
from Utilis.readProperties import ReadConfig
from Configurations.conftest import set_up_tear_down


def test_adhoc_trailer_departure(set_up_tear_down) -> None:
    page = set_up_tear_down
    credentials = {'emailaddress': ReadConfig.getUseremail(), 'password': ReadConfig.getPassword()}
    #Logged Successfully
    login_p = LoginPage(page)
    login_p.do_login(credentials)
    print("Logged in Successfully")

    # Gate Console>> Gate and Site Selected
    gatecons = GateConsole(page)
    gatecons.gateconsole()
    print("Gate Console - Success")

    # Departure of Adhoc Live Trailer
    lvdepart = Gate_Adhoc_Live_Departure(page)
    lvdepart.gate_live_departure(LiveDepartureJSON.getlivedeparturejson())
    print("Departure of Live Trailer")
    time.sleep(5)

    # Departure of Adhoc Drop Trailer
    dddepart = Gate_Adhoc_Drop_Departure(page)
    dddepart.gate_drop_departure(DropDepartureJSON.getdropdeparturejson())
    print("Departure of Drop Trailer")
    time.sleep(5)

