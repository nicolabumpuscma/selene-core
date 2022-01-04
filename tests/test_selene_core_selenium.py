from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException

from selene.core.config import *
from selene.core.selenium.scripts import *

# initialise the driver
driver = get_driver()

# TEST CONDITIONS

def test_bool_url_changed():
    assert True
    
def test_bool_url_expected():
    assert True
    
def test_bool_url_unexpected():
    assert True
    
def test_bool_url_contains():
    assert True
    
def test_bool_url_does_not_contain():
    assert True
    
def test_bool_visible():
    assert True
    
def test_bool_invisible():
    assert True
    
def test_bool_clickable():
    assert True
    
def test_bool_yoffset_changed():
    assert True
    
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