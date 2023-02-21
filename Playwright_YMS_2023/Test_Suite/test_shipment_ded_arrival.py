import json
import time

from Gate.pageObjects.gateconsole import GateConsole
from Gateconsole_Adhoc_Departure.pageObjects.dropdeparture import Gate_Adhoc_Drop_Departure
from Gateconsole_Adhoc_Departure.testCases.test_dropdeparture import DropDepartureJSON
from Gateconsole_Ded_Shipment_Appt_Arrival.pageObjects.ded_droparrival import GateDedDropArrival
from Gateconsole_Ded_Shipment_Appt_Arrival.testCases.test_ded_droparrival import DedDropArrivalJSON
from Login.pageObjects.login import LoginPage
from Shipment.pageObjects.create_dropdelivery_gate_appt import CreateDropDeliveryAppt
from Shipment.testCases.test_dropdelivery_gate_appt import CreateDropDeliveryApptJSON
from Utilis.readProperties import ReadConfig
from Configurations.conftest import set_up_tear_down


def test_ship_dedtrailer_arrival(set_up_tear_down) -> None:
    page = set_up_tear_down
    credentials = {'emailaddress': ReadConfig.getUseremail(), 'password': ReadConfig.getPassword()}
    #Logged Successfully
    login_p = LoginPage(page)
    login_p.do_login(credentials)
    print("Logged in Successfully")


    #Shipment>> Drop Delivery with Appointment
    dropdelappt = CreateDropDeliveryAppt(page)
    dropdelappt.newdropdeliveryappt(CreateDropDeliveryApptJSON.getdropdeliveryapptjson())
    time.sleep(5)
    print("Drop Delivery Shipment created with Appointment")

    # Gate Console>> Gate and Site Selected
    gatecons = GateConsole(page)
    gatecons.gateconsole()
    print("Redirected to Gate Console Screen")

    #Arrival of Shipment with Appt- Dedicated Trailer
    dedarrival = GateDedDropArrival(page)
    dedarrival.deddroparrival(DedDropArrivalJSON.getdroparrivaljson())
    print("Arrival of Shipment with Appt- Dedicated Trailer")
    time.sleep(5)

    #Adhoc Drop Departure
    dddepart = Gate_Adhoc_Drop_Departure(page)
    dddepart.gate_drop_departure(DropDepartureJSON.getdropdeparturejson())
    time.sleep(10)
    print("Departure of Dedicated Trailer")

