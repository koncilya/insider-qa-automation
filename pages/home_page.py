"""
Home Page Object for Insider website
"""

from selenium.webdriver.common.by import By

from config.config import BASE_URL
from pages.base_page import BasePage


class HomePage(BasePage):
    """Page Object for Insider Home Page"""
    
    # Locators
    COMPANY_MENU = (By.XPATH, "//a[contains(text(), 'Company') or contains(@class, 'company')]")
    CAREERS_LINK = (By.XPATH, "//a[contains(text(), 'Careers') or contains(@href, '/careers')]")
    LOGO = (By.CSS_SELECTOR, ".navbar-brand img")
    NAVIGATION_BAR = (By.CSS_SELECTOR, ".navbar-nav:first-child")
    COOKIE_ACCEPT_BUTTON = (By.ID, "wt-cli-accept-all-btn")
    
    def __init__(self, driver):
        """Initialize HomePage with driver"""
        super().__init__(driver)

    def goto_home_page(self):
        """Go to home page"""
        self.driver.get(BASE_URL)
    
    def is_home_page_opened(self):
        """
        Check if Insider home page is opened
        
        Returns:
            bool: True if home page is opened, False otherwise
        """
        try:
            # Check if logo is present
            logo_present = self.is_element_present(self.LOGO)

            # Check if navigation bar is present
            nav_present = self.is_element_present(self.NAVIGATION_BAR)
            
            return logo_present and nav_present
        except Exception as e:
            print(f"Error checking if home page is opened: {e}")
            return False
    
    def hover_over_company_menu(self):
        """Hover over the Company menu"""
        self.hover_over_element(self.COMPANY_MENU)
    
    def click_careers_link(self):
        """Click on the Careers link"""
        self.click_element(self.CAREERS_LINK)
    
    def navigate_to_careers(self):
        """
        Navigate to Careers page by hovering over Company menu and clicking Careers
        
        Returns:
            bool: True if navigation successful, False otherwise
        """
        try:
            self.hover_over_company_menu()
            self.click_careers_link()
            return True
        except Exception as e:
            print(f"Error navigating to careers: {e}")
            return False
    
    def get_page_title(self):
        """
        Get the page title
        
        Returns:
            str: Page title
        """
        return super().get_page_title()
    
    def get_current_url(self):
        """
        Get current URL
        
        Returns:
            str: Current URL
        """
        return super().get_current_url()


    def accept_cookie(self):
        """Accept cookie"""
        self.click_element(self.COOKIE_ACCEPT_BUTTON)
