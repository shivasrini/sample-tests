from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import imp
import sys
import os
import inspect
sys.path.insert(0,os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))

from BasePage import BasePage
HomePageLocators = imp.load_source('HomePageLocators','C:\git\sample-tests\src\Locators\AllLocators.py')
from HomePageLocators import HomePageLocators

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://auth0.com/")

    def navigate_to_trial_signup_page(self):
        self.click(HomePageLocators.SIGN_UP_FOR_TRIAL_BUTTON) 