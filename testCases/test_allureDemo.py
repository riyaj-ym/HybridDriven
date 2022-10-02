import pytest
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By


@allure.severity(allure.severity_level.NORMAL)
class TestAllure:
    @allure.severity(allure.severity_level.MINOR)
    def test_Logo(self, setup, welcome):
        driver = setup
        driver.maximize_window()
        driver.get("https://www.facebook.com/")
        status = driver.find_element(By.XPATH, "//img[@alt='Facebook']").is_displayed()
        if status:
            assert True
        else:
            assert False
        driver.close()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.skip("Skipping this, after fixing issue will run")
    def test_listEmployees(self, setup, welcome):
        pass

    @allure.severity(allure.severity_level.CRITICAL)
    def test_loginNopCom(self, setup, welcome):
        driver = setup
        driver.maximize_window()
        driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
        driver.find_element(By.XPATH, "//input[@id='Email']").clear()
        driver.find_element(By.XPATH, "//input[@id='Email']").send_keys("admin@yourstore.com")

        driver.find_element(By.XPATH, "//input[@id='Password']").clear()
        driver.find_element(By.XPATH, "//input[@id='Password']").send_keys("admin")

        driver.find_element(By.XPATH, "//button[@type='submit']").click()

        exp_Title = "Dashboard / nopCommerce administration1"
        act_Title = driver.title

        if exp_Title == act_Title:
            assert True
            driver.close()
        else:
            allure.attach(driver.get_screenshot_as_png(), name="testLoginScreen", attachment_type=AttachmentType.PNG)
            driver.close()
            assert False



