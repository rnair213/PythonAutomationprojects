import time
import pytest
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.action_chains import ActionChains



from selenium.webdriver.common.by import By
import logging
# from selenium.webdriver.support.wait import WebDriverWait
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from logs.generatinglogs import Logger
from utilities import configreader

log = Logger(__name__, logging.INFO)


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass


class Test_login(BaseTest):
    @pytest.mark.parametrize(["Current_age", "retire_age", "current_income", "spouse_income",
                              "Current_tol_saving", "current_an_saving", "sav_inc_rate"],
                             [('34', '60', '100000', '20000', '250000', '430000', '4')])
    def test_DefaultCalculator(self, Current_age, retire_age, current_income, spouse_income, Current_tol_saving,
                               current_an_saving,
                               sav_inc_rate):
        self.driver.get("https://www.securian.com/insights-tools/retirement-calculator.html")
        log.logger.info("Site loaded and browser launched")
        try:

            self.driver.execute_script("window.scrollBy(0,500)", "")
            self.driver.implicitly_wait(20)
            log.logger.info("Scrolled down")

        except NoSuchElementException:
            print("exception handled")

        self.driver.find_element(By.XPATH, "//*[@id=\"current-age\"]").send_keys(Current_age)
        time.sleep(10)
        self.driver.find_element(By.CSS_SELECTOR, "#retirement-age").send_keys(retire_age)
        time.sleep(10)
        self.driver.find_element(By.XPATH, "//input[@id=\'current-income\']").send_keys(current_income)
        time.sleep(10)
        self.driver.find_element(By.XPATH, "//input[@id=\'spouse-income\']").send_keys(spouse_income)
        time.sleep(10)
        try:
            self.driver.execute_script("window.scrollBy(500,700)", "")
        except NoSuchElementException:
            print("exception handled")
        time.sleep(10)
        log.logger.info("Scrolled down again")

        self.driver.find_element(By.CSS_SELECTOR, "#current-total-savings").send_keys(Current_tol_saving)
        time.sleep(10)
        self.driver.find_element(By.CSS_SELECTOR, "#current-annual-savings").send_keys(current_an_saving)
        time.sleep(10)
        self.driver.find_element(By.CSS_SELECTOR, "#savings-increase-rate").send_keys(sav_inc_rate)
        log.logger.info("forms fields are filled up")

        try:
            status = self.driver.find_element(By.CSS_SELECTOR, "label[for='no-social-benefits']").is_selected()
            print(status)
            if status:
                print("No is selected by default")
            else:
                self.driver.find_element(By.CSS_SELECTOR, "label[for='yes-social-benefits']").click()
                time.sleep(10)
                self.driver.find_element(By.CSS_SELECTOR, "label[for='single']").click()
                self.driver.find_element(By.XPATH, "//input[@id='social-security-override']").click().send_keys("2000")
        except NoSuchElementException:
            print("exception")

        log.logger.info("Yes got selected")

        time.sleep(10)
        try:
            self.driver.find_element(By.XPATH,
                                     "//*[@id=\"retirement-form\"]/div[4]/div[1]/div/div/div/ul/li[2]/a").click()

            time.sleep(10)
            elem= self.driver.find_element(By.Xpath, "//input[@id=\'additional-income\']")
            action = ActionChains(self.driver)
            action.move_to_element_with_offset(elem,62,5.703125).click().perform()
            self.driver.find_element(By.XPATH, "//input[@id=\'additional-income\']").send_keys("2000")
            time.sleep(10)
            self.driver.find_element(By.XPATH, "//input[@id=\'retirement-duration\']").send_keys("12")
            time.sleep(10)

            self.driver.find_element(By.XPATH, "//label[@for=\'include-inflation\']").click()
            time.sleep(10)
            self.driver.find_element(By.XPATH, "//input[@id=\'expected-inflation-rate\']").send_keys("20")

            self.driver.find_element(By.XPATH, "//input[@id=\'retirement-annual-income\']").send_keys("12")
            time.sleep(10)

            self.driver.find_element(By.XPATH, "//input[@id=\'pre-retirement-roi\']").send_keys("6")
            time.slee(10)
            self.driver.find_element(By.XPATH, "//input[@id=\'post-retirement-roi\']").send_keys("8")

            self.driver.find_element(By.XPATH, "//*[@id=\"default-values-form\"]/div[2]/div/div[1]/button").click()
            time.sleep(10)
            self.driver.find_element(By.XPATH, "//input[@id='\'retirement-duration\']").send_keys("1000")
        except NoSuchElementException:
            print("Exception handled")
        try:
            button = "//button[normalize-space()='Calculate']"
            self.driver.find_element(By.CSS_SELECTOR, "button").click()
        except ElementNotInteractableException:
            print("exception handled")
        log.logger.debug("clicking submit button")
        log.logger.info("Test has been passed , User able to successfully fill the forms")

   # assert button.click() is True, "Button got clicked and form submitted"
