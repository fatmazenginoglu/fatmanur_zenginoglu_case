import pytest
import os
from datetime import datetime
import allure
from driver_setup import get_driver  # WebDriver initialization module

def pytest_addoption(parser):
    """Add command-line options for pytest."""
    parser.addoption("--browser", action="store", default="chrome", help="Choose a browser (chrome or firefox)")

@pytest.fixture
def browser(request):
    """Fixture that retrieves the browser type from command-line options."""
    return request.config.getoption("--browser")

@pytest.fixture
def driver(request, browser):
    """Initialize the WebDriver and capture screenshot on failure."""
    driver = get_driver(browser)
    yield driver

    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Capture test results and take a screenshot if the test fails."""
    outcome = yield
    report = outcome.get_result()

    if report.failed and "driver" in item.funcargs:
        driver = item.funcargs["driver"]
        test_name = item.name
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        screenshot_name = f"{test_name}_{timestamp}.png"
        screenshot_path = os.path.join("reports", "screenshots", screenshot_name)

        os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)
        driver.save_screenshot(screenshot_path)

        # Attach screenshot to Allure report
        allure.attach(driver.get_screenshot_as_png(), name=screenshot_name, attachment_type=allure.attachment_type.PNG)
