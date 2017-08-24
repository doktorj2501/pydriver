import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.action_chains import ActionChains as chains

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
        self.test_link = """test-link-id-goes-here"""	
        self.test_link_exp_txt = "expected text goes here"

    def find_exit_modal(self):
        self.exit_modal = self.driver.find_element_by_id("modal-id-goes-here")

    def login(self, un, pw):
        self.driver.get(self.target + '/user/login')
        user_field = self.driver.find_element_by_id("un-field-id")
        user_field.send_keys(un)
        password_field = self.driver.find_element_by_id("pw-field-id")
        password_field.send_keys(pw)
        login_btn = self.driver.find_element_by_id("login-btn-id").click()

    def logout(self):
        user_toolbar = self.driver.find_element_by_id("usr-tb-id").click()
        logout_btn = self.driver.find_element_by_id("logout-btn-id").click()

    def linkcheck(self,elementid,exp_txt):        
        plink = self.driver.find_element_by_xpath(elementid)
        actions = chains(self.driver)
        actions.move_to_element(plink).perform
        link = wait(self.driver, 60).until(EC.element_to_be_clickable((By.ID, elementid)))
        link.click()
        wait(self.driver, 60).until(EC.presence_of_all_elements_located)
        try:
            self.find_exit_modal()
            if self.exit_modal.is_displayed() and self.exit_modal.is_enabled():
                print "Offsite Link Test "
                self.exit_modal.click()
                tot_hand = len(self.driver.window_handles)
                if tot_hand > self.win_hand:
                    self.win_hand = self.win_hand + 1
                    self.driver.switch_to_window(self.driver.window_handles[(tot_hand - 1)])
                    wait(self.driver, 60).until(EC.presence_of_all_elements_located)
        except NoSuchElementException:
            print "Active Exit Modal Not Found "
        bodytext2 = wait(self.driver, 60).until(EC.visibility_of_element_located((By.TAG_NAME,'body'))).text
        self.driver.switch_to_window(self.first_tab)
        self.driver.get(self.target)
        if exp_txt in bodytext2:
            print exp_txt + " found. linkcheck passed!"
            return 1
        print exp_txt + " not found. linkcheck failed!"
        return 0

    def test_search(self,s_terms):
        self.driver.get(self.target + '/search/node')
        search_terms = s_terms
        for idx, val in enumerate(search_terms):
            search_field = self.driver.find_element_by_id("search-field-id-goes-here")
            search_field.send_keys(val)
            search_field.send_keys(Keys.RETURN)
            search_field = self.driver.find_element_by_id("search-field-id-goes-here")
            search_field.clear()
            result = self.driver.find_element_by_xpath("result-xpath-goes-here").text
            assert val in result

        
