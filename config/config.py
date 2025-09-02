"""
Configuration settings for the Insider Test Automation project
"""

from pathlib import Path

# Base URLs
BASE_URL = "https://useinsider.com"
CAREERS_URL = f"{BASE_URL}/careers"
QA_CAREERS_URL = f"{BASE_URL}/careers/quality-assurance"

# Browser Configuration
BROWSER = "chrome"
HEADLESS = True
IMPLICIT_WAIT = 10
PAGE_LOAD_TIMEOUT = 30

# Test Configuration
SCREENSHOT_DIR = Path("screenshots")
REPORT_DIR = Path("reports")

# Test Data
TEST_LOCATION = "Istanbul, Turkiye"
TEST_DEPARTMENT = "Quality Assurance"

# Locator Timeouts
EXPLICIT_WAIT = 10
POLLING_FREQUENCY = 0.5

# Ensure directories exist
SCREENSHOT_DIR.mkdir(exist_ok=True)
REPORT_DIR.mkdir(exist_ok=True)

# Browser Driver Paths (will be auto-managed by webdriver-manager)
CHROME_DRIVER_PATH = None
