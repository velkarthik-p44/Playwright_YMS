import json
import time
from Login.pageObjects.login import LoginPage
from Shipment.pageObjects.create_dropdelivery import CreateDropDelivery
from Utilis.readProperties import ReadConfig
from Configurations.conftest import set_up_tear_down

class CreateDropDeliveryJSON:
    #Create static method
    @staticmethod
    def getdropdeliveryjson():
        myjsonfile=open("C:/Users/VelKarthik/PycharmProjects/Playwright_YMS_2023/Shipment/TestData/createdropdelivery.json", "r")
        jsondata=myjsonfile.read()
        obj=json.loads(jsondata)
        deliverydetails = obj
        return obj

def test_crepickup(set_up_tear_down) -> None:
    page = set_up_tear_down
    credentials = {'emailaddress': ReadConfig.getUseremail(), 'password': ReadConfig.getPassword()}
    login_p = LoginPage(page)
    login_p.do_login(credentials)
    dropdel = CreateDropDelivery(page)
    dropdel.newdropdelivery(CreateDropDeliveryJSON.getdropdeliveryjson())
    time.sleep(5)

