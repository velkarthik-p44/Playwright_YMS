import json
import time
from Login.pageObjects.login import LoginPage
from Shipment.pageObjects.create_droppickup import CreateDropPickupPage

from Utilis.readProperties import ReadConfig
from Configurations.conftest import set_up_tear_down

class CreateDropPickupJSON:
    #Create static method
    @staticmethod
    def getcreatedroppickupjson():
        myjsonfile=open("C:/Users/VelKarthik/PycharmProjects/Playwright_YMS_2023/Shipment/TestData/createdroppickup.json", "r")
        jsondata=myjsonfile.read()
        obj=json.loads(jsondata)
        droppickupdetails = obj
        return obj

def test_droppickup(set_up_tear_down) -> None:
    page = set_up_tear_down
    credentials = {'emailaddress': ReadConfig.getUseremail(), 'password': ReadConfig.getPassword()}
    login_p = LoginPage(page)
    login_p.do_login(credentials)
    drppickup = CreateDropPickupPage(page)
    drppickup.newdroppickup(CreateDropPickupJSON.getcreatedroppickupjson())
    time.sleep(5)

