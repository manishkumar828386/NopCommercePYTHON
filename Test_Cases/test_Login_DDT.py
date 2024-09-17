import time
from math import trunc
import pytest
from openpyxl.chart.trendline import Trendline
from selenium import webdriver
from Page_Objects.LoginPage import LoginPage
from Test_Cases.conftest import setup
from Utils.read_Properties import ReadConfig
from Utils.customLogger import LogGen
from Utils import ExcelUtils


class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = ".//Test_DAta/DDt.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login_DDT(self, setup):
        self.logger.info("*********** Verifying login test 002   **************")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)

        self.rows = ExcelUtils.getRowCount(self.path, "Sheet1")
        print("number of rows :" + str(self.rows))

        lst_status = []

        for r in range(2, self.rows + 1):
            self.user = ExcelUtils.readData(self.path, "Sheet1", r, 1)
            self.password = ExcelUtils.readData(self.path, "Sheet1", r, 2)
            self.expected = ExcelUtils.readData(self.path, "Sheet1", r, 3)

            self.lp.setUserName(self.user)
            self.lp.setUserName(self.password)
            self.lp.clickLogin()

            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Logged In Successfully | Practice Test Automation"

            if act_title == exp_title:
                if self.expected == "Pass":
                    self.logger.info("test is passed")
                    assert True
                    self.lp.clickLogout()
                    lst_status.append("Pass")
                elif self.expected == "Fail":
                    self.lp.clickLogout()
                    self.logger.info("Failed")
                    lst_status.append("Failed")
            elif act_title != exp_title:
                if self.expected == "Pass":
                    self.logger.info("Failed")
                    lst_status.append("Failed")
                elif self.expected == "Fail":
                    self.logger.info("Passed")
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info("************ DDT passed *********")
            self.driver.close()
            assert True
        else:
            self.logger.info("************* DDT Failed **********")
            self.driver.close()
            assert False
