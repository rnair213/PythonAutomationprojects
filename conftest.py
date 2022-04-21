import pytest
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(params=["chrome", "firefox"], scope='class')
def init_driver(request):
    if request.param == "chrome":
        options = Options()
        options.add_argument("--start-maximized")
        web_driver = webdriver.Chrome(chrome_options=options, service=Service(ChromeDriverManager().install()))
    if request.param == "firefox":
        web_driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    request.cls.driver = web_driver

    yield
    web_driver.close()



import logging
from time import asctime


def log():
    logging.basicConfig(filename="logs\\logfile.log", filemode='w', format='%(asctime)s: %(levelname)s: %(message)s'
                        , level=logging.INFO)
    logger = logging.getLogger()
    return logger


logger = log()
logger.info("this is first log")
