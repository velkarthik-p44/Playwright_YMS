import json
import time
from Login.pageObjects.login import LoginPage
from Shipment.pageObjects.create_livedelivery import CreateLiveDelivery

from Utilis.readProperties import ReadConfig
from Configurations.conftest import set_up_tear_down

class CreateLiveDeliveryJSON:
    #Create static method
    @staticmethod
    def getlivedeliveryjson():
        myjsonfile=open("C:/Users/VelKarthik/PycharmProjects/Playwright_YMS_2023/Shipment/TestData/createlivedelivery.json", "r")
        jsondata=myjsonfile.read()
        obj=json.loads(jsondata)
        livedeliverydetails = obj
        return obj

def test_livedelivery(set_up_tear_down) -> None:
    page = set_up_tear_down
    credentials = {'emailaddress': ReadConfig.getUseremail(), 'password': ReadConfig.getPassword()}
    login_p = LoginPage(page)
    login_p.do_login(credentials)
    livedel = CreateLiveDelivery(page)
    livedel.newlivedelivery(CreateLiveDeliveryJSON.getlivedeliveryjson())
    time.sleep(5)

