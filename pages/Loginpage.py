from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self,driver):
        self.driver=driver

    username_xpath='//input[@name="username"]'
    password_xpath='//input[@name="password"]'
    login_btn_xpath="//button[@type='submit']"

    def enter_username(self,username):
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,self.username_xpath)))
        self.driver.find_element(By.XPATH,self.username_xpath).send_keys(username)
    def enter_password(self,password):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.password_xpath)))
        self.driver.find_element(By.XPATH,self.password_xpath).send_keys(password)
    def click_on_login(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.login_btn_xpath)))
        self.driver.find_element(By.XPATH,self.login_btn_xpath).click()