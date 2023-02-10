import json
from Login.pageObjects.login import LoginPage
from Shipment.pageObjects.create_pickup import CreatePickupPage
from Utilis.readProperties import ReadConfig
from Configurations.conftest import set_up_tear_down

class CreatePickupJSON:
    #Create static method
    @staticmethod
    def getcreatepickupjson():
        myjsonfile=open("C:/Users/VelKarthik/PycharmProjects/Playwright_YMS_2023/Shipment/TestData/createpickup.json", "r")
        jsondata=myjsonfile.read()
        obj=json.loads(jsondata)
        pickupdetails = obj
        return obj

def test_crepickup(set_up_tear_down) -> None:
    page = set_up_tear_down
    credentials = {'emailaddress': ReadConfig.getUseremail(), 'password': ReadConfig.getPassword()}
    login_p = LoginPage(page)
    login_p.do_login(credentials)
    pickup = CreatePickupPage(page)
    pickup.newpickup(CreatePickupJSON.getcreatepickupjson())
    # pickup.newpickup()
    page.pause()
