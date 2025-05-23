from selenium import webdriver
import openpyxl
import pytest


@pytest.fixture()
def setup(request):
    driver=webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    request.cls.driver=driver
    yield
    driver.quit()