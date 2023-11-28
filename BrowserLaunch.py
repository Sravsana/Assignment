# Import the 'modules' that are required for execution for Selenium test automation
from telnetlib import EC

import pytest
from selenium import webdriver
import time

from selenium.webdriver.support.wait import WebDriverWait

# Fixture for Chrome
@pytest.fixture(scope="class")
def chrome_driver_init(request):
    chrome_driver = webdriver.Chrome()
    request.cls.driver = chrome_driver
    yield
    chrome_driver.close()


@pytest.mark.usefixtures("driver_init")
class BasicTest:
    pass


class Test_URL(BasicTest):
    def test_open_url(self):
        self.driver.get('https://www.w3schools.com/')
        self.driver.maximize_window()
        title = "W3Schools Online Web Tutorials"
        assert title == self.driver.title

        #Validating the Logo element
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located("//a[@id='w3-logo']"))
        isLogDisplayed = self.driver.find_element_by_xpath("//a[@id='w3-logo']").is_displayed();
        assert isLogDisplayed == True;
        time.sleep(5)

@pytest.mark.usefixtures("chrome_driver_init")
class Basic_Chrome_Test:
    pass

chrome_driver_init()