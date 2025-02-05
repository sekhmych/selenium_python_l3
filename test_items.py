import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_item_page_has_add_to_cart_button(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    time.sleep(3)
    x = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert x is not []
