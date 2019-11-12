import unittest
from selenium import webdriver
import imp

TestData = imp.load_source('TestData','C:\git\sample-tests\src\data\TestData.py')

class TestBase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=TestData.GECKO_EXECUTABLE)
        self.driver.maximize_window

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


