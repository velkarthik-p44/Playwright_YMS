import json
import time
from Login.pageObjects.login import LoginPage
from Shipment.pageObjects.create_livepickup import CreateLivePickupPage
from Utilis.readProperties import ReadConfig
from Configurations.conftest import set_up_tear_down

class CreateLivePickupJSON:
    #Create static method
    @staticmethod
    def getlivepickupjson():
        myjsonfile=open("C:/Users/VelKarthik/PycharmProjects/Playwright_YMS_2023/Shipment/TestData/createlivepickup.json", "r")
        jsondata=myjsonfile.read()
        obj=json.loads(jsondata)
        livepickupdetails = obj
        return obj

def test_createlivepickup(set_up_tear_down) -> None:
    page = set_up_tear_down
    # Login
    credentials = {'emailaddress': ReadConfig.getUseremail(), 'password': ReadConfig.getPassword()}
    login_p = LoginPage(page)
    login_p.do_login(credentials)

    #Create Live Pickup
    livepickup = CreateLivePickupPage(page)
    livepickup.newlivepickup(CreateLivePickupJSON.getlivepickupjson())
    time.sleep(5)

