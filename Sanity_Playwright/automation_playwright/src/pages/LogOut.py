class LoginOut:
    def __init__(self, page):
        self.page = page
        self._logout = page.get_by_role("link", name="John Doe stage mckee mckee - admin")
        self._logoutlink = page.get_by_role("link", name="Logout")
        self._logout_btn = page.get_by_role("link", name="Yes")

    def click_logout(self):
        self._logout.click()

    def click_logoutlink(self):
        self._logoutlink.click()

    def click_logoutbtn(self):
        self._logout_btn.click()