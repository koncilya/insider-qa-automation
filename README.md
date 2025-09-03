# 🚀 Insider Test Automation Project

A comprehensive web automation testing framework built with Python, Selenium, and Pytest for testing the Insider website's career functionality.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Running Tests](#running-tests)
- [Test Cases](#test-cases)
- [Page Object Model](#page-object-model)

## 🎯 Overview

This project automates the testing of Insider's career website functionality, including:
- Home page verification
- Navigation to careers section
- QA job filtering and verification
- Job application redirection validation

The framework uses the Page Object Model (POM) design pattern for maintainable and scalable test automation.

## ✨ Features

- **Page Object Model** - Clean separation of test logic and page interactions
- **Automatic Screenshots** - Screenshots captured on test failures for debugging
- **Configurable Test Data** - Centralized configuration for test parameters
- **Robust Error Handling** - Comprehensive exception handling and logging

## 🔧 Prerequisites

- **Python 3.8+** (Tested with Python 3.13)
- **Chrome Browser** (Latest stable version)
- **Git** (For cloning the repository)

## 📦 Installation

### 1. Clone the Repository
```bash
git clone <git@github.com:koncilya/insider-qa-automation.git>
cd automation-case
```

### 2. Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Verify Installation
```bash
pytest --version
python -c "import selenium; print('Selenium version:', selenium.__version__)"
```

## 🏗️ Project Structure

```
automation-case/
├── config/                     # Configuration files
│   └── config.py              # Test configuration and constants
├── pages/                      # Page Object classes
│   ├── base_page.py           # Base page with common methods
│   ├── home_page.py           # Home page interactions
│   ├── careers_page.py        # Careers page interactions
│   ├── qa_careers_page.py     # QA careers page interactions
│   └── lever_application_page.py # Lever application page
├── utils/                      # Utility functions
│   ├── driver_factory.py      # WebDriver creation and management
│   └── screenshot_utils.py    # Screenshot and wait utilities
├── tests/                      # Test files
│   └── test_insider_automation.py # Main test suite
├── screenshots/                # Screenshots on test failures
├── reports/                    # Test execution reports
├── conftest.py                 # Pytest configuration and fixtures
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

## 🧪 Running Tests

### Run All Tests
```bash
pytest
```

### Run Specific Test
```bash
# Run specific test method
pytest tests/test_insider_automation.py::TestInsiderAutomation::test_01_home_page_opened

# Run specific test class
pytest tests/test_insider_automation.py::TestInsiderAutomation
```

### Run Tests with Verbose Output
```bash
pytest -v
```

### Run Tests with HTML Report
```bash
pytest --html=reports/report.html
```

## 📝 Test Cases

The project includes 5 comprehensive test cases:

### 1. **Home Page Verification**
- **Test**: `test_01_home_page_opened`
- **Purpose**: Verify Insider home page loads correctly
- **Checks**: Logo presence, navigation bar visibility

### 2. **Careers Page Navigation**
- **Test**: `test_02_careers_page_sections`
- **Purpose**: Navigate to careers and verify sections
- **Checks**: Locations, Teams, and Life at Insider sections

### 3. **QA Jobs Filtering**
- **Test**: `test_03_qa_jobs_filtering`
- **Purpose**: Filter QA jobs by location and department
- **Checks**: Job list presence after filtering

### 4. **Job Details Verification**
- **Test**: `test_04_job_details_verification`
- **Purpose**: Verify job details match filter criteria
- **Checks**: Position, department, and location consistency

### 5. **Application Redirection**
- **Test**: `test_05_lever_application_redirection`
- **Purpose**: Verify job application redirection
- **Checks**: Lever application form redirection

## 🎭 Page Object Model

The project implements the Page Object Model pattern for maintainable test code:

### Base Page (`pages/base_page.py`)
- Common web element interactions
- Wait utilities and element verification
- Scroll and hover functionality

### Page Objects
- **HomePage**: Home page navigation and cookie handling
- **CareersPage**: Careers page section verification
- **QACareersPage**: QA careers filtering and job listing
- **LeverApplicationPage**: Application form verification

---

**Happy Testing! 🎉**
