import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
class homepage(object):
    def __init__(self, target, d_c):
        self.win_hand = 0
        self.target = target
        self.driver = webdriver.Remote(
        command_executor = 'http://0.0.0.0:4444/wd/hub',
        desired_capabilities = d_c)
        self.driver.implicitly_wait(60)
        self.driver.get(target)
        self.first_tab = self.driver.current_window_handle
        self.exit_modal_exp_txt = 'Now Leaving'

        self.test_link = """test-link-id-goes-here"""	
        self.test_link_exp_txt = "expected text goes here"
    def find_exit_modal(self):
        self.exit_modal = self.driver.find_element_by_id("modal-id-goes-here")

    def linkcheck(self,elementid,exp_txt):
        win_hand = 0
        link = self.driver.find_element_by_id(elementid)
        link.click()
        time.sleep(1)
        bodytext1 = self.driver.find_element_by_tag_name('body').text
        if self.exit_modal_exp_txt in bodytext1:
            self.find_exit_modal()
            self.exit_modal.click()
        tot_hand = len(self.driver.window_handles)
        if tot_hand > self.win_hand:
            self.win_hand = self.win_hand + 1
            self.driver.switch_to_window(self.driver.window_handles[(tot_hand - 1)])
            time.sleep(1)
        bodytext2 = self.driver.find_element_by_tag_name('body').text
        self.driver.switch_to_window(self.first_tab)
        self.driver.get(self.target)
        if exp_txt in bodytext2:
            print exp_txt + " found. linkcheck passed!"
            return 1
        print exp_txt + " not found. linkcheck failed!"
        return 0
