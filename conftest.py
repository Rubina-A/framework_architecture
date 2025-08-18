import pytest
from selenium import webdriver
from config import settings

@pytest.fixture(scope="session")
def driver():
    if settings.BROWSER == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")
        drv = webdriver.Chrome(options=options)
    else:
        drv = webdriver.Firefox()
    drv.implicitly_wait(settings.IMPLICIT_WAIT)
    yield drv
    drv.quit()
