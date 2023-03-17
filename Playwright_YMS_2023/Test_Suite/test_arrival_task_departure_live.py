import json
import time

from Gate.pageObjects.gateconsole import GateConsole
from Gateconsole_Adhoc_Arrival.pageObjects.livearrival import GateAdhocLiveArrival
from Gateconsole_Adhoc_Arrival.testCases.test_livearrival import LiveArrivalJSON
from Gateconsole_Adhoc_Departure.pageObjects.livedeparture import Gate_Adhoc_Live_Departure
from Gateconsole_Adhoc_Departure.testCases.test_livedeparture import LiveDepartureJSON
from Login.pageObjects.login import LoginPage
from Trailer.pageObjects.trailer_bump import TrailerBump
from Trailer.pageObjects.trailer_listing import TrailerListing
from Trailer.pageObjects.trailer_move import TrailerMove
from Trailer.pageObjects.trailer_pull import TrailerPull
from Trailer.pageObjects.trailer_spot import TrailerSpot
from Trailer.testCases.test_trailer_listing import TrailerListingJSON
from Utilis.readProperties import ReadConfig
from Configurations.conftest import set_up_tear_down


def test_adhoc_trailer_arrival(set_up_tear_down) -> None:
    page = set_up_tear_down
    credentials = {'emailaddress': ReadConfig.getUseremail(), 'password': ReadConfig.getPassword()}
    #Logged Successfully
    login_p = LoginPage(page)
    login_p.do_login(credentials)
    print("Logged in Successfully")
    time.sleep(2)

    # Gate Console>> Gate and Site Selected
    gatecons = GateConsole(page)
    gatecons.gateconsole()
    print("Gate Console - Success")

    # Arrival of Adhoc Live Trailer
    gatela = GateAdhocLiveArrival(page)
    gatela.livearrival(LiveArrivalJSON.getlivearrivaljson())
    print("Adhoc Arrival - Live Trailer")
    time.sleep(2)

    # Trailer Listing
    traillist = TrailerListing(page)
    traillist.trailer_listing(TrailerListingJSON.trailerlistjson())
    print("Trailer Search - Success")
    time.sleep(2)

    # Move Task
    movetrail = TrailerMove(page)
    movetrail.movetrailer()
    print("Move Task has been completed")
    time.sleep(2)

    # Spot Task
    spottrail = TrailerSpot(page)
    spottrail.spottrailer()
    print("Spot Task has been completed")
    time.sleep(2)

    # Bump Task
    bumptrail = TrailerBump(page)
    bumptrail.bumptrailer()
    print("Bump Task has been completed")
    time.sleep(5)

    # Pull Task
    pulltrail = TrailerPull(page)
    pulltrail.pulltrailer()
    print("Pull Task has been completed")
    time.sleep(2)

    # Redirecting to Gate Console Page
    gatecons = GateConsole(page)
    gatecons.saved_gateconsole()
    print("Redirected to Gate Console - Success")
    time.sleep(2)

    # Adhoc Live Departure
    lvdepart = Gate_Adhoc_Live_Departure(page)
    lvdepart.gate_live_departure(LiveDepartureJSON.getlivedeparturejson())
    print("Adhoc Departure - Live Trailer")
    time.sleep(5)