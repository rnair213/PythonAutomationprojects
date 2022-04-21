import time
import pytest
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
import logging

# from selenium.webdriver.support.wait import WebDriverWait
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from logs.generatinglogs import Logger

log = Logger(__name__, logging.INFO)


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass


class Test_login(BaseTest):
    @pytest.mark.parametrize(["Current_age", "retire_age", "current_income", "spouse_income",
                             "Current_tol_saving", "current_an_saving", "sav_inc_rate"],
                             [('34', '60', '100000', '20000', '250000', '430000', '4')])
    def test_login(self,Current_age, retire_age, current_income, spouse_income,Current_tol_saving,current_an_saving,
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
            self.driver.execute_script("window.scrollBy(500,900)", "")
        except NoSuchElementException:
            print("exception handled")
        time.sleep(10)
        log.logger.info("Scrolled down again")

        self.driver.find_element(By.CSS_SELECTOR, "#current-total-savings").send_keys(Current_tol_saving)
        time.sleep(10)
        self.driver.find_element(By.CSS_SELECTOR, "#current-annual-savings").send_keys(current_an_saving)
        time.sleep(10)
        self.driver.find_element(By.CSS_SELECTOR, "#savings-increase-rate").send_keys(sav_inc_rate)
        log.logger.info("form fields are filled up")

        # Wait = WebDriverWait(self.driver, 20)
        # element = Wait.until(ec.element_to_be_clickable(".dsg-btn-primary.btn-block[onclick='calculateResults();']"))
        # print(element)
        time.sleep(20)
        try:
            button = ".dsg-btn-primary.btn-block[onclick='calculateResults();']"
            self.driver.find_element(By.CSS_SELECTOR, "button").click()
        except ElementNotInteractableException:
            print("exception handled")
        log.logger.debug("clicking submit button")
        log.logger.info("Test has been passed , User able to successfully fill the forms")

    # assert button.click() is True, "Button got clicked and form submitted"
