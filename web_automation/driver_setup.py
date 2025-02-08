from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service

def get_driver(browser):
    """Initialize the WebDriver based on the selected browser."""
    if browser.lower() == "chrome":
        options = webdriver.ChromeOptions()  # Create a ChromeOptions instance
        # You can add necessary options for Chrome (e.g., headless mode)
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    elif browser.lower() == "firefox":
        options = webdriver.FirefoxOptions()  # Create a FirefoxOptions instance
        # You can add necessary options for Firefox
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)
    else:
        raise ValueError(f"Invalid browser: {browser}")

    driver.maximize_window()
    return driver
