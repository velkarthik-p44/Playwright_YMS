import pytest

from Utilis.readProperties import ReadConfig

@pytest.fixture
def set_up_tear_down(page) ->None:
    page.set_viewport_size({"width": 1536, "height": 800})
    #page.goto("https:/yard-visibility-na12.voc.qa-stage.p-44.com/auth/login")
    # page.goto(UserLogin.baseURL)
    page.goto(ReadConfig.getApplicationURL())
    page.wait_for_timeout(10000)
    yield page


