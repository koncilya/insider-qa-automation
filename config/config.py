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

# Ensure directories exist
SCREENSHOT_DIR.mkdir(exist_ok=True)
REPORT_DIR.mkdir(exist_ok=True)
