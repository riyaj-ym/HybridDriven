from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest
import allure
from webdriver_manager.chrome import ChromeDriverManager


class TestAllure:
    def test_Logo(self, welcome):
        ser_obj = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=ser_obj)
        self.driver.maximize_window()
        self.driver.get("https://www.facebook.com/")
        self.driver.close()
