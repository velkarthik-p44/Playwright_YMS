import json
import time

from Login.pageObjects.login import LoginPage
from Trailer.pageObjects.trailer_listing import TrailerListing
from Utilis.readProperties import ReadConfig
from Configurations.conftest import set_up_tear_down

class TrailerListingJSON:
    #Create three static methods
    @staticmethod
    def trailerlistjson():
        myjsonfile=open("C:/Users/VelKarthik/PycharmProjects/Playwright_YMS_2023/Trailer/TestData/trailerlisting.json", "r")
        jsondata=myjsonfile.read()
        obj=json.loads(jsondata)
        traillist = obj
        return obj

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
    print("Search the Trailer")
    time.sleep(10)


