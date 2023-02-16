#Contain Test Case for Shipment Creation - Pickup and Delivery
# Load Type : Drop and Live
import json
import time

from Login.pageObjects.login import LoginPage
from Shipment.pageObjects.create_dropdelivery import CreateDropDelivery
from Shipment.pageObjects.create_droppickup import CreateDropPickupPage
from Shipment.pageObjects.create_livedelivery import CreateLiveDelivery
from Shipment.pageObjects.create_livepickup import CreateLivePickupPage
from Shipment.testCases.test_dropdelivery import CreateDropDeliveryJSON
from Shipment.testCases.test_droppickup import CreateDropPickupJSON
from Shipment.testCases.test_livedelivery import CreateLiveDeliveryJSON
from Shipment.testCases.test_livepickup import CreateLivePickupJSON
from Utilis.readProperties import ReadConfig
from Configurations.conftest import set_up_tear_down


def test_shipments(set_up_tear_down) -> None:
    page = set_up_tear_down

    #Log in
    credentials = {'emailaddress': ReadConfig.getUseremail(), 'password': ReadConfig.getPassword()}
    login_p = LoginPage(page)
    login_p.do_login(credentials)

    # Shipment - Live Pickup
    livepickup = CreateLivePickupPage(page)
    livepickup.newlivepickup(CreateLivePickupJSON.getlivepickupjson())
    time.sleep(5)

    # Shipment - Live Delivery
    livedel = CreateLiveDelivery(page)
    livedel.newlivedelivery(CreateLiveDeliveryJSON.getlivedeliveryjson())
    time.sleep(5)

    # Shipment - Drop Pickup
    drppickup = CreateDropPickupPage(page)
    drppickup.newdroppickup(CreateDropPickupJSON.getcreatedroppickupjson())
    time.sleep(5)

    # Shipment - Drop Delivery
    dropdel = CreateDropDelivery(page)
    dropdel.newdropdelivery(CreateDropDeliveryJSON.getdropdeliveryjson())
    time.sleep(5)
