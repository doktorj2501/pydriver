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

class TestDeploy(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Remote(
        command_executor = 'http://0.0.0.0:4444/wd/hub',
        desired_capabilities = d_c
        )
	
    def TestSubs(self):
        driver = self.driver
	prefixes = ['http://subdomain1.','http://subdomain2.']
	pre_pos = 0
	subs_exp_txt = ['sd1 expected text','sd2 expected text']
        for idx, val in enumerate(subs_exp_txt):
            driver.implicitly_wait(60)
	    driver.get(prefixes[pre_pos]+target)
	    bodytext = driver.find_element_by_tag_name('body').text
            assert val in bodytext
	    pre_pos = pre_pos + 1
	    print "Subsite test", pre_pos , "of X passed."
    def tearDown(self):
        self.driver.quit()
