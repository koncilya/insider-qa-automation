"""
WebDriver factory for creating browser instances
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from config.config import BROWSER, HEADLESS, IMPLICIT_WAIT, PAGE_LOAD_TIMEOUT

class DriverFactory:
    """Factory class for creating WebDriver instances"""
    
    @staticmethod
    def get_driver(browser_type=None, headless=None):
        """
        Create and return a WebDriver instance
        
        Args:
            browser_type (str): Browser type (chrome)
            headless (bool): Whether to run in headless mode
            
        Returns:
            WebDriver: Configured WebDriver instance
        """
        browser_type = browser_type or BROWSER
        headless = headless if headless is not None else HEADLESS
        
        if browser_type.lower() == "chrome":
            return DriverFactory._create_chrome_driver(headless)
        else:
            raise ValueError(f"Unsupported browser type: {browser_type}")
    
    @staticmethod
    def _create_chrome_driver(headless):
        """Create Chrome WebDriver"""
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")

        # Try to use system ChromeDriver first, then fallback to webdriver-manager
        try:
            # First try to use system ChromeDriver
            driver = webdriver.Chrome(options=options)
            DriverFactory._configure_driver(driver)
            driver.set_window_size(1920, 1080)
            return driver
        except Exception as system_error:
            print(f"System ChromeDriver not found, trying webdriver-manager: {system_error}")
            try:
                # Use webdriver-manager as fallback
                driver_path = ChromeDriverManager().install()
                # Ensure we get the correct executable path
                if driver_path.endswith('/THIRD_PARTY_NOTICES.chromedriver'):
                    driver_path = driver_path.replace('/THIRD_PARTY_NOTICES.chromedriver', '/chromedriver.exe')
                elif not driver_path.endswith('.exe'):
                    driver_path = driver_path + '.exe'
                
                service = ChromeService(driver_path)
                driver = webdriver.Chrome(service=service, options=options)
                DriverFactory._configure_driver(driver)
                driver.set_window_size(1920, 1080)
                return driver
            except Exception as wdm_error:
                raise Exception(f"Failed to create Chrome driver. System error: {system_error}. WebDriver Manager error: {wdm_error}")
    
    @staticmethod
    def _configure_driver(driver):
        """Configure common driver settings"""
        driver.implicitly_wait(IMPLICIT_WAIT)
        driver.set_page_load_timeout(PAGE_LOAD_TIMEOUT)
        driver.maximize_window()
