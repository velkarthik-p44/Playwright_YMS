from Configurations.config import UserLogin
from automation_playwright.src.pages.Create_PickupPage import CreatePickupPage
from automation_playwright.src.pages.LoginPage import LoginPage
import json
#from ddt import ddt, data, file_data, unpack

#@file_data("../testdata/createpickup.json")

myjsonfile=open("C:/Users/VelKarthik/PycharmProjects/Sanity_Playwright/testdata/createpickup.json","r")
jsondata=myjsonfile.read()

obj=json.loads(jsondata)

def test_crepickup(set_up_tear_down) -> None:
    page = set_up_tear_down
    #credentials = {'emailaddress': 'stagemckeee@yopmail.com', 'password': 'Admin@123'}
    credentials = {UserLogin.emailaddress, UserLogin.password}
    #details = {'Shipment#': 'SHIPM23', 'Ref1': 'refe001', 'Ref2': 'refe002', 'Trailer': 'trai001', 'LP': 'lpl001'}
    details = obj

    login_p = LoginPage(page)
    login_p.do_login(credentials)
    pickup = CreatePickupPage(page)
    pickup.newpickup(details)
    # pickup.newpickup()
