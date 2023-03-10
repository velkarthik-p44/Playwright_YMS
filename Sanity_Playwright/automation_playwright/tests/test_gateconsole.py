from automation_playwright.src.pages.GateConsole import GateConsole
from automation_playwright.src.pages.LoginPage import LoginPage


def test_gateconsole(set_up_tear_down) -> None:
    page = set_up_tear_down
    credentials = {'emailaddress': 'stagemckeee@yopmail.com', 'password': 'Admin@123'}
    login_p = LoginPage(page)
    login_p.do_login(credentials)
    gatecons = GateConsole(page)
    gatecons.gateconsole()
