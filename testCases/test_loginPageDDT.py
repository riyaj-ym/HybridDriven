import time

import pytest

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfigs
from logs.customLogger import LogGen
from utilities.XLUtility import XLUtils


class TestLoginDDT002:
    url = ReadConfigs.getUrl()
    logger = LogGen.logGen()
    file = "./testData/test_loginPageDDT.xlsx"
    sheet = 'Data'
    listStatus = []

    @pytest.mark.critical
    def test_loginDDT(self, setup, welcome):
        self.logger.info("***************** TestLoginDDT002 ***************** ")
        self.logger.info("***************** Verifying LoginPage DDT ***************** ")
        driver = setup
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(self.url)
        lp = LoginPage(driver)
        xl = XLUtils(self.file, self.sheet)
        rows = xl.getRows()
        for r in range(2, rows + 1):
            lp.setUsername(xl.readData(r, 1))
            lp.setPassword(xl.readData(r, 2))
            lp.clickLogin()
            exp = xl.readData(r, 3)

            if driver.title == 'Dashboard / nopCommerce administration':
                if exp == 'Pass':
                    self.logger.info("Passed")
                    self.listStatus.append("Pass")
                    lp.clickLogout()
                elif exp == 'Fail':
                    self.logger.info("Failed")
                    self.listStatus.append("Fail")
                    lp.clickLogout()

            elif driver.title != 'Dashboard / nopCommerce administration':
                if exp == 'Pass':
                    self.logger.info("Failed")
                    self.listStatus.append("Fail")
                elif exp == 'Fail':
                    self.logger.info("Passed")
                    self.listStatus.append("Pass")

        driver.close()

        if 'Fail' not in self.listStatus:
            assert True
            self.logger.info("***************** LoginPage DDT Passed ***************** ")
        else:
            self.logger.info("***************** LoginPage DDT Failed ***************** ")
            assert False

        self.logger.info("***************** LoginPage DDT Completed ***************** ")


fbjhdbnfkdfn
