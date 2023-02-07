from Configurations.config import UserLogin
from automation_playwright.src.pages.Create_PickupPage import CreatePickupPage
from automation_playwright.src.pages.LoginPage import LoginPage
from automation_playwright.src.utilis.readProperties import ReadConfig



def test_loginpage(set_up_tear_down) -> None:
    page = set_up_tear_down
    credentials = {'emailaddress': ReadConfig.getUseremail(), 'password': ReadConfig.getPassword()}
    login_p = LoginPage(page)
    login_p.do_login(credentials)      # Logged Successfully








