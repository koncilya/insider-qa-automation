"""
Base Page Object class that provides common functionality
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains

from utils.screenshot_utils import wait_for_element, wait_for_element_clickable, scroll_to_element


class BasePage:
    """Base class for all page objects"""
    
    def __init__(self, driver):
        """
        Initialize the base page
        
        Args:
            driver: WebDriver instance
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def find_element(self, locator):
        """
        Find a single element
        
        Args:
            locator: Element locator tuple (By, value)
            
        Returns:
            WebElement: Found element
        """
        return self.driver.find_element(*locator)
    
    def find_elements(self, locator):
        """
        Find multiple elements
        
        Args:
            locator: Element locator tuple (By, value)
            
        Returns:
            list: List of found elements
        """
        return self.driver.find_elements(*locator)
    
    def click_element(self, locator, timeout = 10):
        """
        Click on an element

        Args:
            locator: Element locator tuple (By, value)
            timeout: Timeout for click
        """
        try:
            element = wait_for_element_clickable(self.driver, locator, timeout)
            scroll_to_element(self.driver, element)
            element.click()
        except Exception as e:
            raise Exception(f"Failed to click element {locator}: {e}")
    
    def send_keys_to_element(self, locator, text):
        """
        Send text to an element
        
        Args:
            locator: Element locator tuple (By, value)
            text (str): Text to send
        """
        element = wait_for_element(self.driver, locator)
        element.clear()
        element.send_keys(text)
    
    def get_element_text(self, locator):
        """
        Get text from an element
        
        Args:
            locator: Element locator tuple (By, value)
            
        Returns:
            str: Element text
        """
        element = wait_for_element(self.driver, locator)
        print(element.text)
        return element.text.strip()
    
    def is_element_present(self, locator, timeout=5):
        """
        Check if element is present
        
        Args:
            locator: Element locator tuple (By, value)
            timeout (int): Maximum wait time
            
        Returns:
            bool: True if element is present, False otherwise
        """
        try:
            wait_for_element(self.driver, locator, timeout)
            return True
        except TimeoutException:
            return False
    
    def is_element_visible(self, locator, timeout=5):
        """
        Check if element is visible
        
        Args:
            locator: Element locator tuple (By, value)
            timeout (int): Maximum wait time
            
        Returns:
            bool: True if element is visible, False otherwise
        """
        try:
            element = wait_for_element(self.driver, locator, timeout)
            return element.is_displayed()
        except TimeoutException:
            return False
    
    def wait_for_page_load(self):
        """Wait for page to load completely"""
        self.wait.until(
            lambda driver: driver.execute_script("return document.readyState") == "complete"
        )
    
    def get_current_url(self):
        """
        Get current page URL
        
        Returns:
            str: Current URL
        """
        return self.driver.current_url
    
    def get_page_title(self):
        """
        Get page title
        
        Returns:
            str: Page title
        """
        return self.driver.title
    
    def hover_over_element(self, locator):
        """
        Hover over an element
        
        Args:
            locator: Element locator tuple (By, value)
        """
        element = wait_for_element(self.driver, locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
    
    def select_dropdown_option(self, dropdown_locator, option_text):
        """
        Select an option from dropdown by text
        
        Args:
            dropdown_locator: Dropdown element locator
            option_text (str): Text of option to select
        """
        from selenium.webdriver.support.ui import Select
        
        dropdown = wait_for_element(self.driver, dropdown_locator)
        select = Select(dropdown)
        select.select_by_visible_text(option_text)

    def scroll_down(self):
        self.driver.execute_script("window.scrollTo(0, 600);")

