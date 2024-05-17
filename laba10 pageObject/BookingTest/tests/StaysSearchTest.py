import sys
from os.path import dirname, abspath

sys.path.insert(0, dirname(dirname(abspath(__file__))))

import unittest
from selenium import webdriver
from pages.BasePage import BasePage
from pages.Flights import FlightsPage
from pages.StaysPage import StaysPage

class TestStaysSearchTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.BasePage = BasePage(self.driver)
        self.StaysPage = StaysPage(self)
        self.FlightsPage = FlightsPage(self.driver)