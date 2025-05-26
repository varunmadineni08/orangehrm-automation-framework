import pytest

from pages.Adminpage import AdminPage
from pages.Loginpage import LoginPage


@pytest.mark.usefixtures("setup")
class TestLogin:

    def test_admin_add_user(self):
        login_page=LoginPage(self.driver)
        login_page.enter_username("Admin")
        login_page.enter_password("admin123")
        login_page.click_on_login()
        admin_page=AdminPage(self.driver)
        admin_page.click_on_admin_menu()
        # admin_page.click_on_add()
        # admin_page.click_on_ess_role()
        # admin_page.enter_employee_name("a")
        # admin_page.click_on_employee_status()
        # admin_page.enter_emp_username("Arunmotori")
        # admin_page.enter_emp_password("varun1234")
        # admin_page.enter_emp_confirmpassword("varun1234")
        # admin_page.click_on_save()
        admin_page.delete_the_user()
