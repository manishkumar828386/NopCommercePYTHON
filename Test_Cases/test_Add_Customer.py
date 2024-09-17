import string
import time
from math import trunc
from random import random

import pytest
from openpyxl.chart.trendline import Trendline
from selenium import webdriver
from selenium.webdriver.common.by import By

from Page_Objects.AddCustomerPage import AddNewCustomers
from Page_Objects.LoginPage import LoginPage
from Page_Objects.AddCustomerPage import AddNewCustomers
from Test_Cases.conftest import setup
from Utils.read_Properties import ReadConfig
from Utils.customLogger import LogGen


class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getUserPassword()

    logger = LogGen.loggen()


    @pytest.mark.sanity
    def test_addCustomers(self,setup):

        self.logger.info("*** Test 003 started ")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        time.sleep(10)

        self.logger.info("***  login sucessfull ***")

        self.logger.info("***  Adding customer test started ***")

        self.addcust = AddNewCustomers(self.driver)

        self.addcust.click_customerMenu()
        self.addcust.click_customerSubMenu()
        self.addcust.click_AddnewCustomer_btn()

        self.logger.info("*** Providing customer info")

        self.email = self.random_generator() + "gmail.com"
        self.addcust.set_EMail(self.email)
        self.addcust.set_password("test123")
        self.addcust.set_customer_roles("Guest")
        self.addcust.set_Vendor("Vendor 2")
        self.addcust.set_gender("Male")
        self.addcust.set_name("Manish")
        self.addcust.set_LastName("Kumar")
        self.addcust.set_DOB("7/12/1998")
        self.addcust.set_company("BEBO")
        self.addcust.set_AdminComments("This is for testing")
        self.addcust.click_save()

        self.logger.info("*** saving customer info ***")

        self.logger.info("*** add customer validation started ***")

        self.msg = self.driver.find_element(By.TAG_NAME,"body").text

        print(self.msg)

        if "The new customer has been added successfully." == self.msg:
            assert True == True
            self.logger.info("*** Add customer test passed ***")
        else :
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addingcustomer.png")
            self.logger.info("*** add new customer failed")
            assert True == False

        self.driver.close()
        self.logger.info("*** Ending add customer test ***")


    def random_generator(size=8, chars = string.ascii_lowercase + string.digits):
        return "".join(random.choice(chars) for x in range(size))




























