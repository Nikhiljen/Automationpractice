import pytest
from selenium.webdriver.common.by import By

from PageObjects.HomePage import HomePage
from TestData.testdata import HomePageData
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formsubmission(self, getdata):
        log = self.get_logger()
        formsubmit = HomePage(self.driver)
        formsubmit.getname().send_keys(getdata["firstname"])
        formsubmit.getemail().send_keys(getdata["email"])
        formsubmit.getpassword().send_keys(getdata["pass"])
        formsubmit.getCheckBox().click()

        self.select_gender(formsubmit.getgender(), getdata["gender"])
        formsubmit.getStatus().click()
        formsubmit.getsubmit().click()

        successtext = formsubmit.getsuccesmessage().text

        assert "success" in successtext

        self.driver.refresh()

    @pytest.fixture(params=HomePageData.testData)
    def getdata(self,request):
        return request.param
