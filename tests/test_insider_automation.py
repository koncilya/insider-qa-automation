"""
Test cases for Insider Test Automation project
"""
import time

from pages.home_page import HomePage
from pages.careers_page import CareersPage
from pages.qa_careers_page import QACareersPage
from pages.lever_application_page import LeverApplicationPage
from config.config import TEST_LOCATION, TEST_DEPARTMENT

class TestInsiderAutomation:
    """Test class for Insider automation test cases"""
    
    def test_01_home_page_opened(self, driver):
        """
        Test Case 1: Visit https://useinsider.com/ and check Insider home page is opened or not
        """
        home_page = HomePage(driver)

        is_home_page_opened = home_page.is_home_page_opened()

        assert is_home_page_opened, "Insider home page is not opened"
    
    def test_02_careers_page_sections(self, driver):
        """
        Test Case 2: Select the "Company" menu in the navigation bar, select "Careers" 
        and check Career page, its Locations, Teams, and Life at Insider blocks are open or not
        """
        home_page = HomePage(driver)

        navigation_success = home_page.navigate_to_careers()
        assert navigation_success, "Failed to navigate to careers page"

        careers_page = CareersPage(driver)
        careers_page.wait_for_page_load()

        is_careers_page_opened = careers_page.is_careers_page_opened()
        assert is_careers_page_opened, "Careers page is not opened"

        all_sections_visible = careers_page.are_all_sections_visible()

        assert all_sections_visible, "Not all required sections are visible on Careers page"
    
    def test_03_qa_jobs_filtering(self, driver):
        """
        Test Case 3: Go to https://useinsider.com/careers/quality-assurance/, 
        click "See all QA jobs", filter jobs by Location: "Istanbul, Turkey", 
        and Department: "Quality Assurance", check the presence of the job list
        """
        qa_careers_page = QACareersPage(driver)

        qa_careers_page.goto_careers_page()
        qa_careers_page.wait_for_page_load()

        is_qa_page_opened = qa_careers_page.is_qa_careers_page_opened()
        assert is_qa_page_opened, "QA Careers page is not opened"

        qa_careers_page.click_see_all_qa_jobs()
        qa_careers_page.wait_for_page_load()

        time.sleep(2)
        qa_careers_page.apply_filters(TEST_LOCATION, TEST_DEPARTMENT)
        time.sleep(2)

        job_list_present = qa_careers_page.is_job_list_present()
        assert job_list_present, "Job list is not present after filtering"
    
    def test_04_job_details_verification(self, driver):
        """
        Test Case 4: Check that all jobs' Position contains "Quality Assurance", 
        Department contains "Quality Assurance", and Location contains "Istanbul, Turkey"
        """

        # Navigate to QA careers page
        qa_careers_page = QACareersPage(driver)

        qa_careers_page.goto_careers_page()
        qa_careers_page.wait_for_page_load()

        qa_careers_page.click_see_all_qa_jobs()
        qa_careers_page.wait_for_page_load()

        qa_careers_page.apply_filters(TEST_LOCATION, TEST_DEPARTMENT)
        time.sleep(3)

        job_items = qa_careers_page.get_job_items()
        assert len(job_items) > 0, "No job items found to test"

        qa_careers_page.scroll_to_down()
        time.sleep(2)

        departments = []
        locations = []
        for job in job_items:
            department = job.find_element('css selector', ".position-department").text
            location = job.find_element('css selector', ".position-location").text
            departments.append(department)
            locations.append(location)

        assert len(departments) == len(job_items), "Departments do not match job items"
        assert len(locations) == len(job_items), "Locations do not match job items"


    
    def test_05_lever_application_redirection(self, driver):
        """
        Test Case 5: Click the "View Role" button and check that this action 
        redirects us to the Lever Application form page
        """
        qa_careers_page = QACareersPage(driver)

        qa_careers_page.goto_careers_page()
        qa_careers_page.wait_for_page_load()

        qa_careers_page.click_see_all_qa_jobs()
        qa_careers_page.wait_for_page_load()

        qa_careers_page.apply_filters(TEST_LOCATION, TEST_DEPARTMENT)
        time.sleep(3)

        job_items = qa_careers_page.get_job_items()
        assert len(job_items) > 0, "No job items found to test"
        first_job = job_items[0]

        qa_careers_page.scroll_to_down()

        qa_careers_page.hover_over_application_card(first_job)
        time.sleep(2)
        qa_careers_page.click_view_role_button(qa_careers_page.get_first_job_item())

        lever_page = LeverApplicationPage(driver)

        redirection_successful = lever_page.verify_lever_redirection()
        assert redirection_successful, "Redirection to Lever application form failed"
            
