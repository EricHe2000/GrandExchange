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
        print("TitleTest")
        driver = self.driver
        driver.get("http://web:8000")
        self.assertEqual(driver.title, "Grand Exchange")
        self.assertFalse(driver.title == "Error lol")

    #Test to see if when trying to make a new item ... redirects to login page
    def test_not_logged_in(self):

        driver = self.driver
        driver.get("http://web:8000/create/item")
        print("not logged in")

        self.assertTrue("Login" in driver.page_source)

    #test when a user logs in , the logout button appears
    def test_login(self):
        print("creatingLogging")
        driver = self.driver
        driver.get("http://web:8000/create/user")
        driver.find_element_by_name('name').send_keys('Eric')
        driver.find_element_by_name('email').send_keys('eriche2000@gmail.com')
        driver.find_element_by_name('age').send_keys('21')
        driver.find_element_by_name('username').send_keys('12345')
        driver.find_element_by_name('password').send_keys('54321')
        driver.find_element_by_name("login_button").click()
        driver.implicitly_wait(20)
        driver.find_element_by_name('username').send_keys('12345')
        driver.find_element_by_name('password').send_keys('54321')
        driver.find_element_by_name("login_user").click()

        print(driver.page_source)

        self.assertTrue("Logout" in driver.page_source)

    '''
    def test_createListing(self):
        print("creatingListingRunning")
        driver = self.driver
        driver.get("http://web:8000/create/item")
        driver.find_element_by_name('title').send_keys('Test Item')
        driver.find_element_by_name('description').send_keys('Running a test')
        driver.find_element_by_name('price').send_keys('404')
        driver.find_element_by_name('numberBought').send_keys('3')
        driver.find_element_by_xpath("//input[@type='submit'][@value='Ok']").click()
        driver.get("http://web:8000/")
        self.assertTrue("Test Item" in driver.page_source)


    def test_logout(self):
        driver = self.driver
        driver.get("http://web:8000")
        driver.find_element_by_link_text('Create an Account now!').click()

        driver.find_element_by_name("username").send_keys("dustin")
        driver.find_element_by_name("password").send_keys("nguyen")

        driver.find_element_by_name("submit").click()

        driver.find_element_by_link_text('Logout').click()

        self.assertTrue("Already have one? Login Here!" in driver.page_source)
        
    '''

if __name__ == "__main__":
        print("working")
        unittest.main()
