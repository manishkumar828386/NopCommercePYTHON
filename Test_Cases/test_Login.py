import time
from math import trunc
import pytest
from openpyxl.chart.trendline import Trendline
from selenium import webdriver
from Page_Objects.LoginPage import LoginPage
from Test_Cases.conftest import setup
from Utils.read_Properties import ReadConfig
from Utils.customLogger import LogGen


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getUserPassword()

    logger = LogGen.loggen()


    @pytest.mark.regression
    def test_Homepage_title(self, setup):
        self.logger.info("*********** Test 001 Login started  **************")
        self.driver = setup
        self.driver.get(self.baseURL)
        actual_title = self.driver.title
        expectted_title = "Test Login | Practice Test Automation"
        if actual_title == expectted_title:
            assert True
            self.driver.close()
            self.logger.info("*********** Homepage test is passed  **************")
        else :
            self.driver.save_screenshot(".\\Screenshots\\" + "testHomepageTitle.png")
            self.driver.close()
            self.logger.info("*********** Homepage test is failed  **************")
            assert False


    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("*********** Verifying login test   **************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        actTitle = self.driver.title
        exptitle = "Logged In Successfully | Practice Test Automation"
        if actTitle == exptitle:
            self.logger.info("*********** login test passed   **************")
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "login_test.png")
            self.logger.info("*********** login test failed **************")
            self.driver.close()
            assert False