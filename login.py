#!/usr/bin/python
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from testconfig import config

target = config['test_DNs']['test_DN']
username = config['usernames']['username']
password = config['passwords']['password']

if config['browsers']['browser'] == "CHROME":
    d_c = DesiredCapabilities.CHROME
if config['browsers']['browser'] == "FIREFOX":
    d_c = DesiredCapabilities.FIREFOX
if config['browsers']['browser'] == "SAFARI":
    d_c = DesiredCapabilities.SAFARI
if config['browsers']['browser'] == "INTERNETEXPLORER":
    d_c = DesiredCapabilities.INTERNETEXPLORER

class Testlogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Remote(
        command_executor = 'http://0.0.0.0:4444/wd/hub',
        desired_capabilities = d_c
        )
	
    def login(self):
        driver = self.driver
        driver.implicitly_wait(60)
        driver.get(target)
        un_box = driver.find_element_by_id('id-goes-here')
        un_box.send_keys(username)
        pw_box = driver.find_element_by_id('id-goes-here')
        pw_box.send_keys(password)
        login_btn = driver.find_element_by_id('id-goes-here')
        login_btn.click()

    def tearDown(self):
        self.driver.quit()

