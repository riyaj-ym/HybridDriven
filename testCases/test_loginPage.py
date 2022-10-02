import time
import pytest

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfigs
from logs.customLogger import LogGen


class TestLogin001:
    url = ReadConfigs.getUrl()
    username = ReadConfigs.getUsername()
    password = ReadConfigs.getPassword()
    logger = LogGen.logGen()

    @pytest.mark.smoke
    def test_loginPageTitle(self, setup):
        self.logger.info("***************** TestLogin001 ***************** ")
        self.logger.info("***************** Verifying LoginPage Title *****************")
        driver = setup
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(self.url)
        if driver.title == "Your store. Login":
            assert True
            self.logger.info("***************** LoginPage Title Verification Passed *****************")
            print("test_loginPageTitle passed ")
            driver.close()
        else:
            time.sleep(3)
            driver.save_screenshot("./screenshots" + "/test_loginPageTitle.png")
            driver.close()
            self.logger.error("***************** LoginPage Title Verification Failed *****************")
            print("test_loginPageTitle Failed ")
            assert False

    @pytest.mark.regression
    @pytest.mark.smoke
    def test_homePageTitle(self, setup):
        self.logger.info("***************** TestLogin001 ***************** ")
        self.logger.info("***************** Verifying HomePage Title ***************** ")
        driver = setup
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(self.url)
        lp = LoginPage(driver)
        lp.setUsername(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()

        if driver.title == 'Dashboard / nopCommerce administration':
            assert True
            self.logger.info("***************** HomePage Title Verification Passed *****************")
            print("test_homePageTitle Passed ")
            driver.close()
        else:
            time.sleep(3)
            driver.save_screenshot("./screenshots" + "/test_homePageTitle.png")
            lp.clickLogout()
            driver.close()
            self.logger.error("***************** HomePage Title Verification Failed *****************")
            print("test_homePageTitle Failed ")
            assert False
