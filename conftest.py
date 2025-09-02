"""
Pytest configuration file for Insider Test Automation project
Handles WebDriver lifecycle + screenshot on failure
"""

import pytest

from pages.home_page import HomePage
from utils.driver_factory import DriverFactory
from utils.screenshot_utils import take_screenshot
from config.config import BROWSER, HEADLESS


@pytest.fixture(scope="function")
def driver():
    """
    WebDriver fixture: creates a new driver instance for each test
    and quits safely after test finishes
    """
    driver = None
    try:
        # Create driver
        driver = DriverFactory.get_driver(BROWSER, HEADLESS)
        yield driver
    except Exception as e:
        print(f"[!] Error during driver setup: {e}")
        if driver:
            driver.quit()
        raise
    finally:
        if driver:
            try:
                driver.quit()
            except Exception as e:
                print(f"[!] Error closing driver: {e}")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Automatically take screenshot if a test fails
    """
    outcome = yield
    result = outcome.get_result()

    if result.when == "call" and result.failed:
        driver = item.funcargs.get("driver", None)
        if driver:
            test_name = item.name
            try:
                take_screenshot(driver, test_name)
                print(f"\n[!] Screenshot taken for failed test: {test_name}")
            except Exception as e:
                print(f"[!] Failed to take screenshot: {e}")

@pytest.fixture(autouse=True)
def accept_cookies_before_test(driver):
    """
    Her test başlamadan önce cookie banner varsa kabul eder
    """
    home_page = HomePage(driver)
    home_page.goto_home_page()
    home_page.wait_for_page_load()
    try:
        home_page.accept_cookie()
    except Exception:
        pass