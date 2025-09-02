"""
Lever Application Page Object for verifying redirection from job listing
"""

from pages.base_page import BasePage


class LeverApplicationPage(BasePage):
    """Page Object for Lever Application Form Page"""

    # Page verification
    LEVER_URL_CONTAINS = "jobs.lever.co"
    
    def __init__(self, driver):
        """Initialize LeverApplicationPage with driver"""
        super().__init__(driver)
    
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

        return self.LEVER_URL_CONTAINS in current_url