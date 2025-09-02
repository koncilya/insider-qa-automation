"""
QA Careers Page Object for Insider website
"""
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config.config import TEST_LOCATION, TEST_DEPARTMENT, QA_CAREERS_URL


class QACareersPage(BasePage):
    """Page Object for Insider QA Careers Page"""
    
    # Locators
    SEE_ALL_QA_JOBS_BUTTON = (By.XPATH, "//a[contains(text(), 'See all QA jobs') or contains(text(), 'See all QA')]")
    
    # Filter locators
    LOCATION_FILTER = (By.XPATH, "//select[contains(@name, 'location') or contains(@id, 'location') or contains(@class, 'location')]")
    DEPARTMENT_FILTER = (By.XPATH, "//select[contains(@name, 'department') or contains(@id, 'department') or contains(@class, 'department')]")
    
    # Alternative filter locators
    LOCATION_FILTER_ALT = (By.XPATH, "//div[contains(@class, 'filter')]//select[contains(., 'Location') or contains(., 'location')]")
    DEPARTMENT_FILTER_ALT = (By.XPATH, "//div[contains(@class, 'filter')]//select[contains(., 'Department') or contains(., 'department')]")
    
    # Job list locators
    JOB_LIST_CONTAINER = (By.XPATH, "//div[contains(@class, 'job-list') or contains(@class, 'jobs') or contains(@class, 'careers')]")
    JOB_ITEMS = (By.CLASS_NAME, "position-list .position-list-item")
    JOB_ITEM_FIRST = (By.CLASS_NAME, "position-list .position-list-item:first-child")
    
    # Job detail locators
    JOB_POSITION = (By.XPATH, ".//h3[contains(@class, 'title') or contains(@class, 'position')] | .//div[contains(@class, 'title')]")
    JOB_DEPARTMENT = (By.XPATH, ".//div[contains(@class, 'department') or contains(@class, 'team')]")
    JOB_LOCATION = (By.XPATH, ".//div[contains(@class, 'location') or contains(@class, 'place')]")
    VIEW_ROLE_BUTTON = (By.XPATH, ".//a[contains(text(), 'View Role') or contains(@class, 'apply') or contains(@class, 'view')]")
    PAGINATE_BUTTON = (By.XPATH, "//*[@id=\"pagination\"]/div/div/div[2]/ul/div/button[2]")

    # Page verification
    PAGE_TITLE_CONTAINS = "Quality Assurance"
    URL_CONTAINS = "/careers/quality-assurance"

    APPLICATION_CARD = (By.XPATH, "//*[@id=\"jobs-list\"]/div[1]/div")
    
    def __init__(self, driver):
        """Initialize QACareersPage with driver"""
        super().__init__(driver)

    def goto_careers_page(self):
        """Go to QA Careers page"""
        self.driver.get(QA_CAREERS_URL)

    def is_qa_careers_page_opened(self):
        """
        Check if QA Careers page is opened

        Returns:
            bool: True if QA Careers page is opened, False otherwise
        """
        try:
            current_url = self.get_current_url()
            page_title = self.get_page_title()

            url_correct = self.URL_CONTAINS in current_url
            title_correct = self.PAGE_TITLE_CONTAINS.lower() in page_title.lower()

            return url_correct and title_correct
        except Exception as e:
            print(f"Error checking if QA careers page is opened: {e}")
            return False
    
    def click_see_all_qa_jobs(self):
        """Click on 'See all QA jobs' button"""
        self.click_element(self.SEE_ALL_QA_JOBS_BUTTON)
    
    def filter_by_location(self, location=TEST_LOCATION):
        """
        Filter jobs by location
        
        Args:
            location (str): Location to filter by
        """
        try:
            # Try primary location filter
            if self.is_element_present(self.LOCATION_FILTER):
                self.select_dropdown_option(self.LOCATION_FILTER, location)
            elif self.is_element_present(self.LOCATION_FILTER_ALT):
                self.select_dropdown_option(self.LOCATION_FILTER_ALT, location)
            else:
                print("Location filter not found")
        except Exception as e:
            print(f"Error filtering by location: {e}")
            raise
    
    def filter_by_department(self, department=TEST_DEPARTMENT):
        """
        Filter jobs by department
        
        Args:
            department (str): Department to filter by
        """
        try:
            # Try primary department filter
            if self.is_element_present(self.DEPARTMENT_FILTER):
                self.select_dropdown_option(self.DEPARTMENT_FILTER, department)
            elif self.is_element_present(self.DEPARTMENT_FILTER_ALT):
                self.select_dropdown_option(self.DEPARTMENT_FILTER_ALT, department)
            else:
                print("Department filter not found")
        except Exception as e:
            print(f"Error filtering by department: {e}")
            raise
    
    def apply_filters(self, location=TEST_LOCATION, department=TEST_DEPARTMENT):
        """
        Apply both location and department filters
        
        Args:
            location (str): Location to filter by
            department (str): Department to filter by
        """
        self.filter_by_location(location)
        self.filter_by_department(department)
    
    def is_job_list_present(self):
        """
        Check if job list is present after filtering
        
        Returns:
            bool: True if job list is present, False otherwise
        """
        try:
            return self.is_element_present(self.JOB_LIST_CONTAINER) and len(self.find_elements(self.JOB_ITEMS)) > 0
        except Exception as e:
            print(f"Error checking job list: {e}")
            return False
    
    def get_job_items(self):
        """
        Get all job items from the list
        
        Returns:
            list: List of job item elements
        """
        try:
            return self.find_elements(self.JOB_ITEMS)
        except Exception as e:
            print(f"Error getting job items: {e}")
            return []

    def get_first_job_item(self):
        """
        Get all job items from the list

        Returns:
            list: List of job item elements
        """
        try:
            return self.find_element(self.JOB_ITEM_FIRST)
        except Exception as e:
            print(f"Error getting job item: {e}")
            return []
    
    def verify_job_details(self, job_item):
        """
        Verify job details for a specific job item
        
        Args:
            job_item: WebElement representing a job item
            
        Returns:
            dict: Dictionary with verification results
        """
        try:
            # Get job details
            position = job_item.find_element(*self.JOB_POSITION).text.strip()
            department = job_item.find_element(*self.JOB_DEPARTMENT).text.strip()
            location = job_item.find_element(*self.JOB_LOCATION).text.strip()
            
            # Verify details
            position_correct = TEST_DEPARTMENT in position
            department_correct = TEST_DEPARTMENT in department
            location_correct = TEST_LOCATION in location
            
            return {
                'position_correct': position_correct,
                'department_correct': department_correct,
                'location_correct': location_correct,
                'position': position,
                'department': department,
                'location': location
            }
        except Exception as e:
            print(f"Error verifying job details: {e}")
            return {
                'position_correct': False,
                'department_correct': False,
                'location_correct': False,
                'position': 'N/A',
                'department': 'N/A',
                'location': 'N/A'
            }
    
    def verify_all_jobs(self):
        """
        Verify all jobs in the list meet the requirements
        
        Returns:
            bool: True if all jobs are verified, False otherwise
        """
        job_items = self.get_job_items()
        if not job_items:
            print("No job items found")
            return False
        
        all_verified = True
        for i, job_item in enumerate(job_items):
            print(f"\nVerifying job {i+1}:")
            verification = self.verify_job_details(job_item)
            
            print(f"Position: {verification['position']} - {'✓' if verification['position_correct'] else '✗'}")
            print(f"Department: {verification['department']} - {'✓' if verification['department_correct'] else '✗'}")
            print(f"Location: {verification['location']} - {'✓' if verification['location_correct'] else '✗'}")
            
            if not all([verification['position_correct'], verification['department_correct'], verification['location_correct']]):
                all_verified = False
        
        return all_verified
    
    def click_view_role_button(self, job_item):
        """
        Click View Role button for a specific job item
        
        Args:
            job_item: WebElement representing a job item
        """
        try:
            view_role_button = job_item.find_element(*self.VIEW_ROLE_BUTTON)
            view_role_button.click()
        except Exception as e:
            print(f"Error clicking View Role button: {e}")
    
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

    def hover_over_application_card(self, element):
        """Hover over the Company menu"""
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
