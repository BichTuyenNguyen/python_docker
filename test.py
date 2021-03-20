import time
import pytest
from hamcrest import assert_that, equal_to
from selenium import webdriver


@pytest.fixture()
def web_driver():
    driver_lst = []

    def _web_driver(browser_name):
        grid_url = 'http://{host}:{port}/wd/hub'.format(host='localhost', port='4444')
        caps = {
            'browserName': browser_name
        }
        browser = webdriver.Remote(grid_url, desired_capabilities=caps)
        driver_lst.append(browser)

        browser.set_page_load_timeout(10)
        browser.maximize_window()

        return browser

    yield _web_driver
    driver_lst[0].quit()


def test_1(web_driver):
    driver = web_driver('chrome')
    driver.get('https://www.google.com/')
    time.sleep(3)
    assert_that(driver.title, equal_to('Google'), 'Verify the title')


def test_2(web_driver):
    driver = web_driver('firefox')
    driver.get('https://www.google.com/')
    time.sleep(3)
    assert_that(driver.title, equal_to('Google'), 'Verify the title')
