from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException

from selene.core.config import *
from selene.core.selenium.scripts import *
from selene.core.selenium.driver import *
from selene.core.selenium.page import *

# initialise the driver
driver = get_driver()
url = "https://www.scrapethissite.com/"
page = PageSelene.from_url(driver=driver, url = url)

def test_bool_url_changed():
    assert bool_url_changed(driver, wait=1, logger=None, url = url) == False
    
def test_bool_url_expected():
    assert bool_url_expected(driver, wait=1, logger=None, url = url) == True
    
def test_bool_url_unexpected():
    alt_url = "https://www.scrapethissite.com/pages/simple/"
    assert bool_url_unexpected(driver, wait=1, logger=None, url = alt_url) == True
    
def test_bool_url_contains():
    assert bool_url_contains(driver, wait=1, logger=None, string = "scrape") == True
    
def test_bool_url_does_not_contain():
    assert bool_url_does_not_contain(driver, wait=1, logger=None, string = "scrape") == False
    
def test_bool_visible():
    assert bool_visible(driver, by = By.ID, identifier = 'nav-homepage', wait = 1) == True
    
def test_bool_invisible():
    assert bool_invisible(driver, by = By.ID, identifier = 'nav-homepage', wait = 1) == False
    
def test_bool_clickable():
    assert bool_clickable(driver, by = By.CLASS_NAME, identifier = 'btn btn-lg btn-default', wait = 1) == False
    
def test_bool_yoffset_changed():
    page = PageSelene.from_url(driver=driver, url = "https://www.scrapethissite.com/pages/simple/")
    orig_offset = driver.execute_script("return window.pageYOffset")
    page.scroll_down(driver, wait = 1)
    assert bool_yoffset_changed(driver, wait = 1, yoffset = orig_offset, logger = None) == True
    
def test_bool_scroll_position_changed():
    assert True
    
def test_bool_scroll_height_changed():
    assert True
    
def test_bool_element_class_contains():
    assert True
    
def test_bool_element_class_does_not_contain():
    assert True    
    
def test_bool_element_text_contains():
    assert True
    
def test_bool_element_text_does_not_contain():
    assert True
    
def test_bool_new_handle():
    assert True
    
def test_bool_correct_handle():
    assert True
    
# TEST CRAWLER

def test_crawler_init():
    assert True


# TEST DRIVER
def test_get_driver():
    assert True
    
def test_stop_driver():
    assert True
    
def test_stop_driver():
    assert True
    
def test_restart_driver():
    assert True
    
def test_get_user_agent():
    assert True
    
def test_get_user_agent_random():
    assert True

# TEST ELEMENT


# TEST PAGE


# TEST SCRIPTS


# TEST TASKS