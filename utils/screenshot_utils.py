"""
Utility functions for taking screenshots
"""

from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from config.config import SCREENSHOT_DIR

def take_screenshot(driver, test_name):
    """
    Take a screenshot and save it with timestamp
    
    Args:
        driver: WebDriver instance
        test_name (str): Name of the test for filename
        
    Returns:
        str: Path to the saved screenshot
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{test_name}_{timestamp}.png"
    filepath = SCREENSHOT_DIR / filename
    
    try:
        driver.save_screenshot(str(filepath))
        print(f"Screenshot saved: {filepath}")
        return str(filepath)
    except Exception as e:
        print(f"Failed to take screenshot: {e}")
        return None


def wait_for_element(driver, locator, timeout=10):
    """
    Wait for an element to be present and visible
    
    Args:
        driver: WebDriver instance
        locator: Element locator tuple (By, value)
        timeout (int): Maximum wait time in seconds
        
    Returns:
        WebElement: Found element
        
    Raises:
        TimeoutException: If element is not found within timeout
    """
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
        return element
    except TimeoutException:
        raise TimeoutException(f"Element {locator} not found within {timeout} seconds")


def wait_for_element_clickable(driver, locator, timeout=10):
    """
    Wait for an element to be clickable
    
    Args:
        driver: WebDriver instance
        locator: Element locator tuple (By, value)
        timeout (int): Maximum wait time in seconds
        
    Returns:
        WebElement: Clickable element
        
    Raises:
        TimeoutException: If element is not clickable within timeout
    """
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        return element
    except TimeoutException:
        raise TimeoutException(f"Element {locator} not clickable within {timeout} seconds")


def scroll_to_element(driver, element):
    """
    Scroll to make an element visible
    
    Args:
        driver: WebDriver instance
        element: WebElement to scroll to
    """
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    driver.execute_script("window.scrollBy(0, -100);")
