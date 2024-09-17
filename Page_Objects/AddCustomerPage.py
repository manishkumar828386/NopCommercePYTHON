import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class AddNewCustomers:
    link_customerOption_Xpath = "//i[@class='nav-icon far fa-user']"
    link_customerSubMenu_XPATH = "//p[text()=' Customers']"
    btn_AddnewCustomer_XPath = "//i[@class='fas fa-plus-square']"

    txtBox_Email_XPATH = "//*[@id='Email']"
    txtBox_passeord_XPATH = "//*[@id='Password']"
    txtBox_Name_XPATH = "//*[@id='FirstName']"
    txtBox_Last_Name_XPATH = "//*[@id='LastName']"

    radio_male_Xpath = "//*[@id='Gender_Male']"
    radio_female_Xpath = "//*[@id='Gender_Female']"

    txtBox_DOB_XPATH = "//*[@id='DateOfBirth']"
    txtBox_Company_XPATH = "//*[@id='Company']"

    txtBox_Newsletter_XPATH = "//input[@type='search' and @role='searchbox' and @class='select2-search__field valid']"

    lstItem_admin_Xpath = "//li[text()='Administrators']"
    lstItem_formvendor_Xpath = "//li[text()='Forum Moderators']"
    lstItem_Registered_Xpath = "//li[text()='Registered']"
    lstItem_Vendors_Xpath = "//li[text()='Vendors']"
    lstItem_Guests_Xpath = "//li[text()='Guests']"

    txtBox_Customer_Role_XPATH = "//ul[@class='select2-selection__rendered']"
    drpdwn_selectVendors_XPATH = "//*[@id='VendorId']"
    txtBox_adminCOmments_XPATH = "//*[@id='AdminComment']"
    btn_Save_XPATH = "//button[@type='submit' and @name='save']"



    # =============

    def __init__(self, driver):
        self.driver = driver

    # ---------
    def click_customerMenu(self):
        self.driver.find_Element(By.XPATH, self.link_customerOption_Xpath).click()

    def click_customerSubMenu(self):
        self.driver.find_Element(By.XPATH, self.link_customerSubMenu_XPATH).click()

    def click_AddnewCustomer_btn(self):
        self.driver.find_Element(By.XPATH, self.btn_AddnewCustomer_XPath).click()

    def set_EMail(self, email):
        self.driver.find_Element(By.XPATH, self.txtBox_Email_XPATH).send_keys(email)

    def set_password(self, password):
        self.driver.find_Element(By.XPATH, self.txtBox_passeord_XPATH).send_keys(password)

    def set_name(self, name):
        self.driver.find_Element(By.XPATH, self.txtBox_Name_XPATH).send_keys(name)

    def set_LastName(self, lstName):
        self.driver.find_Element(By.XPATH, self.txtBox_Last_Name_XPATH).send_keys(lstName)

    def set_gender(self, gender):
        if gender == "Male":
            self.driver.find_Element(By.XPATH, self.radio_male_Xpath).click()
        elif gender == "Female":
            self.driver.find_Element(By.XPATH, self.radio_female_Xpath).click()
        else:
            self.driver.find_Element(By.XPATH, self.radio_male_Xpath).click()

    def set_DOB(self, dob):
        self.driver.find_Element(By.XPATH, self.txtBox_DOB_XPATH).send_keys(dob)

    def set_company(self, company):
        self.driver.find_Element(By.XPATH, self.txtBox_Company_XPATH).send_keys(company)

    def set_Newslettwe(self,newsletter):
        self.driver.find_Element(By.XPATH, self.txtBox_Newsletter_XPATH).send_keys(newsletter)


    def set_customer_roles(self, role):
        self.driver.find_Element(By.XPATH, self.txtBox_Customer_Role_XPATH).click()
        time.sleep(3)

        if role == "Administrators":
            self.listItme = self.driver.find_Element(By.XPATH, self.lstItem_admin_Xpath)
        elif role == "Forum Moderators":
            self.listItme = self.driver.find_Element(By.XPATH, self.lstItem_formvendor_Xpath)
        elif role == "Registered":
            self.listItme = self.driver.find_Element(By.XPATH, self.lstItem_Registered_Xpath)
        elif role == "Vendors":
            self.listItme = self.driver.find_Element(By.XPATH, self.lstItem_Vendors_Xpath)
        elif role == "Guests":
            self.listItme = self.driver.find_Element(By.XPATH, self.lstItem_Guests_Xpath)
        else:
            self.listItme = self.driver.find_Element(By.XPATH, self.lstItem_Registered_Xpath)

        time.sleep(3)
        self.driver.execute_script("arguments[0]", self.listItme)

    def set_Vendor(self, vendor):
        drp = Select(self.driver.find_Element(By.XPATH, self.drpdwn_selectVendors_XPATH))
        drp.select_by_visible_text(vendor)

    def set_AdminComments(self, comments):
        self.driver.find_Element(By.XPATH, self.txtBox_adminCOmments_XPATH).send_keys(comments)

    def click_save(self):
        self.driver.find_Element(By.XPATH, self.btn_Save_XPATH).click()
    link_customer_Xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a/p/text()"
