from selenium.webdriver.common.by import By

from PageObjects.CheckoutPage import check_Out_Page


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")  # shop is class variable if you want to use it used by HomePage.shop
    name = (By.CSS_SELECTOR, "[name='name']")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    checkbox = (By.ID, "exampleCheck1")
    gender = (By.CSS_SELECTOR, "select[class='form-control']")
    employee_status = (By.ID, "inlineRadio1")
    submit = (By.CSS_SELECTOR, "input[type='submit']")
    success = (By.CSS_SELECTOR, "[class*='alert-success'")

    def shopItem(self):
        self.driver.find_element(*HomePage.shop).click()
        # DESERIALIZED TUPLE
        # driver.find_element(By.CSS_SELECTOR,"a[href*='/angularpractice/shop']").click()
        checkoutpage = check_Out_Page(self.driver)
        return checkoutpage

    def getname(self):
        return self.driver.find_element(*HomePage.name)

    def getemail(self):
        return self.driver.find_element(*HomePage.email)

    def getpassword(self):
        return self.driver.find_element(*HomePage.password)

    def getCheckBox(self):
        return self.driver.find_element(*HomePage.checkbox)

    def getgender(self):
        return self.driver.find_element(*HomePage.gender)

    def getStatus(self):
        return self.driver.find_element(*HomePage.employee_status)

    def getsubmit(self):
        return self.driver.find_element(*HomePage.submit)

    def getsuccesmessage(self):
        return self.driver.find_element(*HomePage.success)
