import json
import time
from Login.pageObjects.login import LoginPage
from Shipment.pageObjects.create_droppickup import CreateDropPickupPage

from Utilis.readProperties import ReadConfig
from Configurations.conftest import set_up_tear_down

class CreatePickupJSON:
    #Create static method
    @staticmethod
    def getcreatepickupjson():
        myjsonfile=open("C:/Users/VelKarthik/PycharmProjects/Playwright_YMS_2023/Shipment/TestData/createpickup.json", "r")
        jsondata=myjsonfile.read()
        obj=json.loads(jsondata)
        droppickupdetails = obj
        return obj

def test_createdroppickup(set_up_tear_down) -> None:
    page = set_up_tear_down
    credentials = {'emailaddress': ReadConfig.getUseremail(), 'password': ReadConfig.getPassword()}
    login_p = LoginPage(page)
    login_p.do_login(credentials)
    pickup = CreateDropPickupPage(page)
    pickup.newdroppickup(CreatePickupJSON.getcreatepickupjson())
    time.sleep(5)

