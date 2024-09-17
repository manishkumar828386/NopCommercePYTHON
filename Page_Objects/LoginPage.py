from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    textbox_Email_xpath = "//*[@id='Email']"
    textbox_password_ID = "Password"
    button_submit_xpath = "//button[@class='button-1 login-button']"
    button_logout_XPATH = "//*[@id='loop-container']/div/article/div[2]/div/div/div/a"


    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element(By.XPATH, self.textbox_Email_xpath).clear()
        self.driver.find_element(By.XPATH,self.textbox_Email_xpath).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element(By.ID, self.textbox_password_ID).clear()
        self.driver.find_element(By.ID, self.textbox_password_ID).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_submit_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.button_logout_XPATH).click()
