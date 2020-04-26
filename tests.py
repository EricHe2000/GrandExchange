import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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
    
    def login(self):
        driver = self.driver
        driver.get("http://web:8000/create/user")
        driver.find_element_by_name('name').send_keys('Eric')
        driver.find_element_by_name('email').send_keys('eriche2000@gmail.com')
        driver.find_element_by_name('age').send_keys('21')
        driver.find_element_by_name('username').send_keys('12345')
        driver.find_element_by_name('password').send_keys('54321')
        driver.implicitly_wait(20)
        driver.find_element_by_name('username').send_keys('12345')
        driver.find_element_by_name('password').send_keys('54321')
        driver.get("http://web:8000/")
        self.assertTrue("Logout" in driver.page_source)