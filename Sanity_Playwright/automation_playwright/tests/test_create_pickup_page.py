from automation_playwright.src.pages.Create_PickupPage import CreatePickupPage
from automation_playwright.src.pages.LoginPage import LoginPage


def test_crepickup(set_up_tear_down) -> None:
    page = set_up_tear_down
    credentials = {'emailaddress': 'stagemckeee@yopmail.com', 'password': 'Admin@123'}
    details = {'Shipment#': 'SHIPM002', 'Ref1': 'refe001', 'Ref2': 'refe002', 'Trailer': 'trai001', 'LP': 'lpl001'}
    login_p = LoginPage(page)
    login_p.do_login(credentials)
    pickup = CreatePickupPage(page)
    pickup.newpickup(details)
    # pickup.newpickup()
