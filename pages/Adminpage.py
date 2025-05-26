from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from selenium.webdriver import ActionChains


class AdminPage:
    def __init__(self,driver):
        self.driver=driver

    #adding user
    admin_menu_xpath='//span[text()="Admin"]'
    # add_button_xpath='//i[contains(@class,"oxd-button-icon")]'
    # user_role_xpath='(//div)[@class="oxd-select-text oxd-select-text--active"][1]'
    # ess_xpath='//div[@role="listbox"]//div[contains(@class, "oxd-select-option")]'
    # employee_name_xpath='//input[@placeholder="Type for hints..."]'
    # employee_name_list_xpath='//div[@role="listbox"]//div[contains(@class, "oxd-autocomplete-dropdown")][1]'
    #
    # emp_status_xpath='(//div)[@class="oxd-select-text oxd-select-text--active"][2]'
    # emp_enabled_xpath = '//div[@role="listbox"]//div[contains(@class,"oxd-select-option")]'
    #
    #
    # emp_username_xpath='(//input)[3]'
    # emp_password_xpath='(//input)[@type="password"][1]'
    # emp_confirm_password_xpath='(//input)[@type="password"][2]'
    # save_btn_xpath='//button[@type="submit"]'

    #deleting the user as admin
    # table_class='oxd-table'
    expected_emp="manda user"
    delete_btn_xpath='//div[@class="oxd-table"]//i[@class="oxd-icon bi-trash"]/preceding::div[text()="'+expected_emp+'"]'



    def click_on_admin_menu(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,self.admin_menu_xpath))).click()
        # self.driver.find_element(By.XPATH,self.admin_menu_xpath).click()

    # def click_on_add(self):
    #     WebDriverWait(self.driver, 10).until(
    #         EC.visibility_of_element_located((By.XPATH,self.add_button_xpath))).click()
    #     # self.driver.find_element(By.XPATH,self.add_button_xpath).click()
    #
    # def click_on_ess_role(self):
    #     dropdown = WebDriverWait(self.driver, 10).until(
    #         EC.element_to_be_clickable((By.XPATH, self.user_role_xpath))
    #     )
    #     dropdown.click()
    #
    #     options = WebDriverWait(self.driver, 10).until(
    #         EC.visibility_of_all_elements_located((By.XPATH, self.ess_xpath))
    #     )
    #     for option in options:
    #         if option.text.strip() == "ESS":
    #             option.click()
    #             break
    #
    # def enter_employee_name(self,emp_name):
    #     name=WebDriverWait(self.driver, 10).until(
    #         EC.visibility_of_element_located((By.XPATH, self.employee_name_xpath)))
    #     name.send_keys(emp_name)
    #     name_suggestion=WebDriverWait(self.driver, 10).until(
    #         EC.visibility_of_element_located((By.XPATH, self.emp_status_xpath)))
    #     name_suggestion.click()
    #
    #     # self.driver.find_element(By.XPATH, self.employee_name_xpath)
    #     # self.driver.find_element(By.XPATH, self.employee_name_list_xpath).click()
    #
    # def click_on_employee_status(self):
    #     dropdown2 = WebDriverWait(self.driver, 10).until(
    #         EC.element_to_be_clickable((By.XPATH, self.emp_status_xpath))
    #     )
    #     dropdown2.click()
    #
    #     options1 = WebDriverWait(self.driver, 10).until(
    #         EC.visibility_of_all_elements_located((By.XPATH, self.emp_enabled_xpath))
    #     )
    #     for option1 in options1:
    #         if option1.text.strip() == "Enabled":
    #             actions=ActionChains(self.driver)
    #             actions.move_to_element(option1).click().perform()
    #             break
    #
    #     # self.driver.find_element(By.XPATH, self.emp_enabled_xpath).click()
    #
    # def enter_emp_username(self,emp_username):
    #     self.driver.find_element(By.XPATH,self.emp_username_xpath).send_keys(emp_username)
    #
    # def enter_emp_password(self, emp_password):
    #     self.driver.find_element(By.XPATH, self.emp_password_xpath).send_keys(emp_password)
    #
    # def enter_emp_confirmpassword(self, emp_confirmpassword):
    #     self.driver.find_element(By.XPATH, self.emp_confirm_password_xpath).send_keys(emp_confirmpassword)
    #
    # def click_on_save(self):
    #     self.driver.find_element(By.XPATH,self.save_btn_xpath).click()

    def delete_the_user(self):
        delete_user=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,self.delete_btn_xpath)))
        delete_user.click()

