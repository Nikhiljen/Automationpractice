from selenium.webdriver.common.by import By
from PageObjects.ConfirmPage import conFirmPage


class check_Out_Page:

    def __init__(self, driver):
        self.driver = driver

    card_title = (By.CSS_SELECTOR, ".card-title a")
    card_footer = (By.CSS_SELECTOR, ".card-footer button")
    check_out_page = (By.XPATH, "//button[@class='btn btn-success']")

    def get_card_Title(self):
        return self.driver.find_elements(*check_Out_Page.card_title)

    def get_card_footer(self):
        return self.driver.find_elements(*check_Out_Page.card_footer)

    def check_out_Items(self):
        self.driver.find_element(*check_Out_Page.check_out_page).click()
        confirm_page = conFirmPage(self.driver)
        return confirm_page
