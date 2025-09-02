"""
Careers Page Object for Insider website
"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CareersPage(BasePage):
    """Page Object for Insider Careers Page"""
    
    # Locators for main sections
    LOCATIONS_SECTION = (By.ID, "career-our-location")
    TEAMS_SECTION = (By.ID, "career-find-our-calling")
    LIFE_AT_INSIDER_SECTION = (By.CLASS_NAME, "elementor-widget-wrap.elementor-element-populated.e-swiper-container")

    # Alternative locators for sections
    LOCATIONS_HEADER = (By.CLASS_NAME, "#career-our-location .category-title-media")
    TEAMS_HEADER = (By.CLASS_NAME, "#career-find-our-calling .category-title-media")
    LIFE_HEADER = (By.CLASS_NAME, "elementor-widget-wrap.elementor-element-populated.e-swiper-container .elementor-widget-heading")
    
    # Page title and URL verification
    PAGE_TITLE_CONTAINS = "Careers"
    URL_CONTAINS = "/careers"
    
    def __init__(self, driver):
        """Initialize CareersPage with driver"""
        super().__init__(driver)
    
    def is_careers_page_opened(self):
        """
        Check if Careers page is opened
        
        Returns:
            bool: True if Careers page is opened, False otherwise
        """
        try:
            current_url = self.get_current_url()
            page_title = self.get_page_title()
            
            url_correct = self.URL_CONTAINS in current_url
            title_correct = self.PAGE_TITLE_CONTAINS in page_title
            
            return url_correct and title_correct
        except Exception as e:
            print(f"Error checking if careers page is opened: {e}")
            return False
    
    def is_locations_section_visible(self):
        """
        Check if Locations section is visible
        
        Returns:
            bool: True if Locations section is visible, False otherwise
        """
        try:
            return (self.is_element_visible(self.LOCATIONS_SECTION) or 
                   self.is_element_visible(self.LOCATIONS_HEADER))
        except Exception as e:
            print(f"Error checking locations section: {e}")
            return False
    
    def is_teams_section_visible(self):
        """
        Check if Teams section is visible
        
        Returns:
            bool: True if Teams section is visible, False otherwise
        """
        try:
            return (self.is_element_visible(self.TEAMS_SECTION) or 
                   self.is_element_visible(self.TEAMS_HEADER))
        except Exception as e:
            print(f"Error checking teams section: {e}")
            return False
    
    def is_life_at_insider_section_visible(self):
        """
        Check if Life at Insider section is visible
        
        Returns:
            bool: True if Life at Insider section is visible, False otherwise
        """
        try:
            return (self.is_element_visible(self.LIFE_AT_INSIDER_SECTION) or 
                   self.is_element_visible(self.LIFE_HEADER))
        except Exception as e:
            print(f"Error checking life at insider section: {e}")
            return False
    
    def are_all_sections_visible(self):
        """
        Check if all required sections are visible
        
        Returns:
            bool: True if all sections are visible, False otherwise
        """
        locations_visible = self.is_locations_section_visible()
        teams_visible = self.is_teams_section_visible()
        life_visible = self.is_life_at_insider_section_visible()
        
        return locations_visible and teams_visible and life_visible
    
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
