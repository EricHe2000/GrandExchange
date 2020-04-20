import unittest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class BasicWebTestCase(unittest.TestCase):
    # setUp method is called before each test in this class

    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor='http://selenium-chrome:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME)

    #Test that the link leads to correct page with title
    def test_title_check(self):
        driver = self.driver
        driver.get("http://web:8000")
        self.assertEqual(driver.title, "GrandExchange")
        self.assertFalse(driver.title == "Error lol")