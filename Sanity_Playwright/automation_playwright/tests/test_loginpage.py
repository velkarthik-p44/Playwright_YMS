from automation_playwright.src.pages.Create_PickupPage import CreatePickupPage
from automation_playwright.src.pages.LoginPage import LoginPage


def test_loginpage(set_up_tear_down) -> None:
    page = set_up_tear_down
    credentials = {'emailaddress': 'stagemckeee@yopmail.com', 'password': 'Admin@123'}
    login_p = LoginPage(page)
    login_p.do_login(credentials)







