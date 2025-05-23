import pytest
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.Loginpage import LoginPage
from utils.excelreader import get_login_data


@pytest.mark.parametrize("username,password,test_type",get_login_data())
@pytest.mark.usefixtures('setup')
class TestLogin:

    def test_login_page(self,username,password,test_type):
        login_page=LoginPage(self.driver)
        login_page.enter_username(username)
        login_page.enter_password(password)
        login_page.click_on_login()
        if test_type.lower() == 'valid':
            try:
                # Wait for Dashboard heading to appear
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, '//h6[text()="Dashboard"]'))
                )
                print("✅ Valid login successful.")
            except TimeoutException:
                assert False, "❌ Dashboard not found — valid login failed."
        else:
            error_message = ""
            try:
                error_element = WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, '//p[text()="Invalid credentials"]'))
                )
                error_message = error_element.text.lower()
            except TimeoutException:
                try:
                    required_element = WebDriverWait(self.driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, '//span[text()="Required"]'))
                    )
                    error_message = required_element.text.lower()
                except TimeoutException:
                    assert False, "❌ No error message found for invalid login"

            assert 'invalid credentials' in error_message or 'required' in error_message
            print(f"✅ Error message shown as expected: {error_message}")