from Configurations.config import UserLogin
from automation_playwright.src.pages.Create_PickupPage import CreatePickupPage
from automation_playwright.src.utilis.customeLogger import LogGen


class LoginPage:
    def __init__(self, page):
        self.page = page
        self._emailaddress = page.get_by_label("Email Address")
        self._password = page.get_by_label("Password")
        self._login_btn = page.get_by_text("Login")





    def enter_emailaddress(self, email):
        self._emailaddress.clear()
        self._emailaddress.fill(email)

    def enter_password(self, pwd):
        self._password.fill(pwd)

    def click_login(self):
        self._login_btn.click()

    def do_login(self, credentials):

        self.enter_emailaddress(credentials['emailaddress'])
        self.enter_password(credentials['password'])
        self.click_login()


    # def do_login( self, emailaddress, password ):
    #     self.enter_emailaddress(emailaddress)
    #     self.enter_password(password)
    #     self.click_login()





