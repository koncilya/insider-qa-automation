"""
Lever Application Page Object for verifying redirection from job listing
"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LeverApplicationPage(BasePage):
    """Page Object for Lever Application Form Page"""
    
    # Locators for Lever application page
    LEVER_FORM = (By.XPATH, "//form[contains(@class, 'lever-form') or contains(@action, 'lever')]")
    APPLY_BUTTON = (By.XPATH, "//button[contains(text(), 'Apply') or contains(@class, 'apply')]")
    JOB_TITLE = (By.XPATH, "//h1[contains(@class, 'job-title') or contains(@class, 'title')]")
    
    # Alternative locators
    LEVER_CONTAINER = (By.XPATH, "//div[contains(@class, 'lever') or contains(@id, 'lever')]")
    APPLICATION_FORM = (By.XPATH, "//div[contains(@class, 'application') or contains(@class, 'form')]")
    
    # Page verification
    LEVER_URL_CONTAINS = "jobs.lever.co"
    LEVER_TITLE_CONTAINS = "Lever"
    
    def __init__(self, driver):
        """Initialize LeverApplicationPage with driver"""
        super().__init__(driver)
    
    def is_lever_application_page_opened(self):
        """
        Check if Lever application page is opened
        
        Returns:
            bool: True if Lever application page is opened, False otherwise
        """
        try:
            current_url = self.get_current_url()
            page_title = self.get_page_title()
            
            # Check if redirected to Lever domain
            url_correct = self.LEVER_URL_CONTAINS in current_url
            
            # Check if page title contains Lever
            title_correct = self.LEVER_TITLE_CONTAINS in page_title
            
            # Check if application form is present
            form_present = self.is_element_present(self.LEVER_FORM) or self.is_element_present(self.LEVER_CONTAINER)
            
            print(f"URL contains Lever domain: {url_correct}")
            print(f"Title contains Lever: {title_correct}")
            print(f"Application form present: {form_present}")
            
            return url_correct and title_correct and form_present
        except Exception as e:
            print(f"Error checking if Lever application page is opened: {e}")
            return False
    
    def is_application_form_visible(self):
        """
        Check if application form is visible
        
        Returns:
            bool: True if application form is visible, False otherwise
        """
        try:
            return (self.is_element_visible(self.LEVER_FORM) or 
                   self.is_element_visible(self.LEVER_CONTAINER) or
                   self.is_element_visible(self.APPLICATION_FORM))
        except Exception as e:
            print(f"Error checking application form: {e}")
            return False
    
    def get_job_title_from_form(self):
        """
        Get job title from the application form
        
        Returns:
            str: Job title or empty string if not found
        """
        try:
            if self.is_element_present(self.JOB_TITLE):
                return self.get_element_text(self.JOB_TITLE)
            return ""
        except Exception as e:
            print(f"Error getting job title from form: {e}")
            return ""
    
    def is_apply_button_present(self):
        """
        Check if Apply button is present
        
        Returns:
            bool: True if Apply button is present, False otherwise
        """
        try:
            return self.is_element_present(self.APPLY_BUTTON)
        except Exception as e:
            print(f"Error checking Apply button: {e}")
            return False
    
    def verify_lever_redirection(self):
        """
        Verify that the page has been redirected to Lever application form
        
        Returns:
            bool: True if redirection is successful, False otherwise
        """

        # Wait for page to load
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])

        self.wait_for_page_load()

        current_url = self.get_current_url()

        return "lever.co" in current_url


    
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
