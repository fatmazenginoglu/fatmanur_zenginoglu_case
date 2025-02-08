import pytest
from driver_setup import get_driver  # Import the driver_setup module

def pytest_addoption(parser):
    """Add command-line options for pytest."""
    parser.addoption("--browser", action="store", default="chrome", help="Choose a browser (chrome or firefox)")

@pytest.fixture
def browser(request):
    """Fixture that passes the browser information to tests and displays it in the terminal."""
    browser_name = request.config.getoption("--browser")
    print(f"\nBrowser in use: {browser_name}")
    return browser_name

@pytest.fixture
def driver(browser):
    """Initialize the WebDriver and quit it after the test completes."""
    driver = get_driver(browser)
    yield driver
    driver.quit()
