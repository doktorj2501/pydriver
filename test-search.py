#!/usr/bin/python
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from testconfig import config
 
target = config['test_DNs']['test_DN']
if config['browsers']['browser'] == "CHROME":
    d_c = DesiredCapabilities.CHROME
if config['browsers']['browser'] == "FIREFOX":
    d_c = DesiredCapabilities.FIREFOX
if config['browsers']['browser'] == "SAFARI":
    d_c = DesiredCapabilities.SAFARI
if config['browsers']['browser'] == "INTERNETEXPLORER":
    d_c = DesiredCapabilities.INTERNETEXPLORER
 
class TestSearch(unittest.TestCase):
 
    def setUp(self):
        self.driver = webdriver.Remote(
        command_executor = 'http://0.0.0.0:4444/wd/hub',
        desired_capabilities = d_c
        )
 
    def test_search(self):
        search_terms = ['search','terms','go','here']
        driver = self.driver
        driver.implicitly_wait(60)
        driver.get(target+'/search/')
        driver.maximize_window()
 
        for idx, val in enumerate(search_terms):
            search_field = driver.find_element_by_id('search-field-id')
            search_field.send_keys(val)
            search_field.send_keys(Keys.RETURN)
            search_field = driver.find_element_by_id('search-field-id')
            search_field.clear()
            bodytext = driver.find_element_by_tag_name('body').text
            assert val in bodytext
    def tearDown(self):
        self.driver.quit()
