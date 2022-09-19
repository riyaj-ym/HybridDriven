import pytest
from selenium import webdriver


@pytest.fixture()
def setup(browser):
    if browser == 'firefox':
        from selenium.webdriver.firefox.service import Service
        ops = webdriver.FirefoxOptions()
        # ops.headless = True
        ser_oj = Service("E:/Practice/Python/Hybrid FrameWork/Web Drivers/geckodriver.exe")
        driver = webdriver.Firefox(service=ser_oj, options=ops)
        return driver

    elif browser == 'edge':
        from selenium.webdriver.edge.service import Service
        ops = webdriver.EdgeOptions()
        # ops.headless = True
        ser_oj = Service("E:/Practice/Python/Hybrid FrameWork/Web Drivers/msedgedriver.exe")
        driver = webdriver.Edge(service=ser_oj, options=ops)
        return driver

    else:
        from selenium.webdriver.chrome.service import Service
        ops = webdriver.ChromeOptions()
        # ops.headless = True
        ser_oj = Service("E:/Practice/Python/Hybrid FrameWork/Web Drivers/chromedriver.exe")
        driver = webdriver.Chrome(service=ser_oj, options=ops)
        return driver


def pytest_addoption(parser):  # This will get the value from CLI/hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the browser value to set up method
    return request.config.getoption("--browser")


# Pytest HTML Report

def pytest_configure(config):
    config._metadata['Project Name'] = 'Nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tested By'] = 'Riyaj M'


# It is hooks for delete/modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
