import time

import pytest

from pages.ProductPage import ProductPage
from pages.LoginPage import LoginPage
from pages.MainPage import MainPage
from pages.locators import ProductPageLocators


@pytest.mark.xfail(strict=True)
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    item_page = ProductPage(browser, link)
    item_page.open()
    item_page.add_to_card()
    item_page.is_not_element_present(
        *ProductPageLocators.SUCCESS_ADD_PRODUCT_TO_BASKET_TEXT)


def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    item_page = ProductPage(browser, link)
    item_page.open()
    item_page.is_not_element_present(
        *ProductPageLocators.SUCCESS_ADD_PRODUCT_TO_BASKET_TEXT)


@pytest.mark.xfail(strict=True)
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    item_page = ProductPage(browser, link)
    item_page.open()
    item_page.add_to_card()
    item_page.is_disappeared(
        *ProductPageLocators.SUCCESS_ADD_PRODUCT_TO_BASKET_TEXT)

@pytest.mark.skip
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_link()

@pytest.mark.skip
@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        print()
        login_page.should_be_login_page()

    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()
