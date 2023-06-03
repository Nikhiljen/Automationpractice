import pytest
from selenium import webdriver
import time

from selenium.webdriver.common.by import By

from PageObjects.CheckoutPage import check_Out_Page
from PageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):
    def test_e2e(self):
        log = self.get_logger()
        homePage = HomePage(self.driver)
        check_out_page = homePage.shopItem()

        cards = check_out_page.get_card_Title()
        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            log.info(cardText)
            if cardText == "BlackBerry":
                check_out_page.get_card_footer()[i].click()

        self.driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()

        confirm_page = check_out_page.check_out_Items()
        log.info("Entering a country name as ind")
        self.driver.find_element(By.ID, "country").send_keys("ind")
        self.verify_Link("India")
        self.driver.find_element(By.LINK_TEXT, "India").click()
        self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element(By.CSS_SELECTOR, "[class='btn btn-success btn-lg']").click()
        alert_text = self.driver.find_element(By.CSS_SELECTOR, "[class*='alert-success']").text
        log.info("Text received from application is "+alert_text)

        assert ("Success! Thank you!" in alert_text)