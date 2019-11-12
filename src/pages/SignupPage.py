from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import imp
import imp
import sys
import os
import inspect
sys.path.insert(0,os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))

from BasePage import BasePage
SignUpPageLocators = imp.load_source('SignUpPageLocators','C:\git\sample-tests\src\Locators\AllLocators.py')
from SignUpPageLocators import SignUpPageLocators

class SignupPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def fill_in_email_address(self,emailAddress):
        self.enter_text(SignUpPageLocators.EMAIL_TEXT_BOX,emailAddress)

    def fill_in_password(self,password):
        self.enter_text(SignUpPageLocators.PASSWORD_TEXT_BOX,password)

    def signup(self):
        self.click(SignUpPageLocators.SIGN_UP_BUTTON) 

    def error_message_displayed(self):
        self.is_visible(SignUpPageLocators.ERROR_MESSAGE_DIV)