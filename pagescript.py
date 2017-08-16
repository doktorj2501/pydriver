#!/usr/bin/python
import unittest
import time
from testconfig import config
from pageobj import homepage
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

target = config['test_DNs']['test_DN']
if config['browsers']['browser'] == "CHROME":
    chopt = webdriver.ChromeOptions()
    chopt.add_argument('--start-maximized')
    chopt.add_argument('--ignore-certificate-errors')
    chopt.add_argument('--allow-running-insecure-content')
    d_c = chopt.to_capabilities()    
if config['browsers']['browser'] == "FIREFOX":
    d_c = DesiredCapabilities.FIREFOX
if config['browsers']['browser'] == "SAFARI":
    d_c = DesiredCapabilities.SAFARI
if config['browsers']['browser'] == "INTERNETEXPLORER":
    d_c = DesiredCapabilities.INTERNETEXPLORER

class TestJC(unittest.TestCase):
    def testSuccess(self):
        num_tests = 1
        tt = success_homepage(target,d_c)
        results = [2] * num_tests
        res_pos = 0
        if d_c == DesiredCapabilities.FIREFOX or d_c == DesiredCapabilities.INTERNETEXPLORER or d_c == DesiredCapabilities.SAFARI:
            tt.driver.maximize_window()

        results[res_pos] = tt.linkcheck(tt.test_link,tt.test_link_exp_txt)
        res_pos = res_pos + 1
        
        #after all tests
        tt.driver.quit()
        for idx, val in enumerate(results):
            assert val != 0
