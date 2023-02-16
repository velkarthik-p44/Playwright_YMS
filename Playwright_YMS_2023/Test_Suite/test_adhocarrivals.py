#Contain Test Case for Adhoc/Non-Dedicated Trailer Arrivals
#Includes Live, Drop and Drop Hook

import json
import time

from Gate.pageObjects.gateconsole import GateConsole
from Gateconsole_Adhoc_Arrival.pageObjects.droparrival import GateAdhocDropArrival
from Gateconsole_Adhoc_Arrival.pageObjects.drophookarrival import GateAdhocDropHook
from Gateconsole_Adhoc_Arrival.pageObjects.livearrival import GateAdhocLiveArrival
from Gateconsole_Adhoc_Arrival.testCases.test_droparrival import DropArrivalJSON
from Gateconsole_Adhoc_Arrival.testCases.test_drophookarrival import DropHookJSON
from Gateconsole_Adhoc_Arrival.testCases.test_livearrival import LiveArrivalJSON
from Login.pageObjects.login import LoginPage
from Utilis.readProperties import ReadConfig
from Configurations.conftest import set_up_tear_down


def test_adhoc_trailer_arrival(set_up_tear_down) -> None:
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

    # Arrival of Adhoc Live Trailer
    gatela = GateAdhocLiveArrival(page)
    gatela.livearrival(LiveArrivalJSON.getlivearrivaljson())
    print("Arrival of Live Trailer")
    time.sleep(5)


    # Arrival of Adhoc Drop Trailer
    gateda = GateAdhocDropArrival(page)
    gateda.droparrival(DropArrivalJSON.getdroparrivaljson())
    print("Arrival of Drop Trailer")
    time.sleep(5)

    # Arrival of Adhoc Drop Hook Trailer(Empty Pickup)
    gatedh = GateAdhocDropHook(page)
    gatedh.drophookarrival(DropHookJSON.getdrophookjson())
    print("Arrival of Drophook Trailer")
    time.sleep(5)