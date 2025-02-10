from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    """ Insider Home Page Operations """

    def __init__(self, driver):
        self.driver = driver
        self.home_url = "https://useinsider.com/"
        self.company_menu = (By.XPATH, "//a[contains(text(),'Company')]")
        self.careers_link = (By.XPATH, "//a[contains(text(),'Careers')]")  # 'careers_menu' replaced with 'careers_link'

    def open_home_page(self):
        """Navigate to the Insider homepage and verify it is opened."""
        self.driver.get(self.home_url)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.company_menu))

        # Validation: Check if the page is redirected to the correct URL
        assert self.driver.current_url == self.home_url, (
            f"ERROR: Home page URL mismatch! Expected: {self.home_url}, Found: {self.driver.current_url}"
        )

    def go_to_careers_page(self):
        """Click on the 'Company' menu and navigate to the 'Careers' page."""
        company_menu = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.company_menu))
        company_menu.click()

        # 'careers_menu' was incorrect, replaced with 'careers_link'
        careers_link = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.careers_link))
        careers_link.click()

        # Validation: Ensure the page is correctly redirected to the "careers" URL
        WebDriverWait(self.driver, 10).until(lambda d: "careers" in d.current_url.lower())
        assert "careers" in self.driver.current_url.lower(), (
            f"ERROR: Failed to navigate to Careers page! Current URL: {self.driver.current_url}"
        )
