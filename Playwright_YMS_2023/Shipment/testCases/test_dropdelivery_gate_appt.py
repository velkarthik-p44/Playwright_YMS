import time
import json
from Login.pageObjects.login import LoginPage
from Shipment.pageObjects.create_dropdelivery_gate_appt import CreateDropDeliveryAppt
from Utilis.readProperties import ReadConfig
from Configurations.conftest import set_up_tear_down


class CreateDropDeliveryApptJSON:
    #Create static method
    @staticmethod
    def getdropdeliveryapptjson():
        myjsonfile=open("C:/Users/VelKarthik/PycharmProjects/Playwright_YMS_2023/Shipment/TestData/createdropdelivery_gate_appt.json", "r")
        jsondata=myjsonfile.read()
        obj=json.loads(jsondata)
        dropdeliveryappt = obj
        return obj

def test_dropdeliveryappt(set_up_tear_down) -> None:
    page = set_up_tear_down
    credentials = {'emailaddress': ReadConfig.getUseremail(), 'password': ReadConfig.getPassword()}
    #Logged In
    login_p = LoginPage(page)
    login_p.do_login(credentials)

    #Drop Delivery Shipment - Gate Appt
    dropdelappt = CreateDropDeliveryAppt(page)
    dropdelappt.newdropdeliveryappt(CreateDropDeliveryApptJSON.getdropdeliveryapptjson())
    time.sleep(5)

