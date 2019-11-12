import unittest
from selenium import webdriver
import imp

HomePage = imp.load_source('HomePage','C:\git\sample-tests\src\pages\HomePage.py')
SignupPage = imp.load_source('SignupPage','C:\git\sample-tests\src\pages\SignupPage.py')

from HomePage import HomePage
from SignupPage import SignupPage

class WhenAnInvalidUserTriesToSignUp(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path="C:\drivers\geckodriver.exe")
        self.driver.maximize_window

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

    def test_login_fails(self):
        self.homePage = HomePage(self.driver)
        self.homePage.navigate_to_trial_signup_page()
        self.trialSignupPage = SignupPage(self.driver)
        self.trialSignupPage.fill_in_email_address("x@x.com")
        self.trialSignupPage.fill_in_password("###")
        self.assertTrue(self.trialSignupPage.error_message_displayed)

if __name__ == "__main__":
    unittest.main()