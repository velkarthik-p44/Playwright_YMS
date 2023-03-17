                # Test Case - Complete Task Activity includes Move, Spot, Bump, Pull

import json
import time

from Login.pageObjects.login import LoginPage
from Trailer.pageObjects.trailer_bump import TrailerBump
from Trailer.pageObjects.trailer_listing import TrailerListing
from Trailer.pageObjects.trailer_move import TrailerMove
from Trailer.pageObjects.trailer_pull import TrailerPull
from Trailer.pageObjects.trailer_spot import TrailerSpot
from Trailer.testCases.test_trailer_listing import TrailerListingJSON
from Utilis.readProperties import ReadConfig
from Configurations.conftest import set_up_tear_down

def test_trailer_listing(set_up_tear_down) -> None:
    page = set_up_tear_down
    #Login
    credentials = {'emailaddress': ReadConfig.getUseremail(), 'password': ReadConfig.getPassword()}
    login_p = LoginPage(page)
    login_p.do_login(credentials)
    print("Logged in Successfully")
    time.sleep(5)

    #Trailer Listing
    traillist = TrailerListing(page)
    traillist.trailer_listing(TrailerListingJSON.trailerlistjson())
    print("Trailer Search")
    time.sleep(5)

    # Move Task
    movetrail = TrailerMove(page)
    movetrail.movetrailer()
    print("Move Task has been completed")
    time.sleep(5)

    #Spot Task
    spottrail = TrailerSpot(page)
    spottrail.spottrailer()
    print("Spot Task has been completed")
    time.sleep(5)

    # Bump Task
    bumptrail = TrailerBump(page)
    bumptrail.bumptrailer()
    print("Bump Task has been completed")
    time.sleep(5)

    # Pull Task
    pulltrail = TrailerPull(page)
    pulltrail.pulltrailer()
    print("Pull Task has been completed")
    time.sleep(5)
