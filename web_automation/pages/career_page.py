from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

def soft_assert(condition, message, errors, driver, step_name):
    """Soft assertion: Save the error message and take a screenshot if the condition fails."""
    if not condition:
        errors.append(message)  # Add the error message to the list
        
        # Ensure the screenshot folder exists
        if not os.path.exists("reports/screenshots"):
            os.makedirs("reports/screenshots")

        # Save screenshot
        screenshot_path = f"reports/screenshots/{step_name}.png"
        driver.save_screenshot(screenshot_path)
        print(f" ERROR: {message} - Screenshot saved: {screenshot_path}")

class CareerPage:
    """Insider career page operations."""

    def __init__(self, driver):
        self.driver = driver
        self.errors = []  # List to store errors
        self.qa_jobs_button = (By.XPATH, "//a[contains(text(),'See all QA jobs')]")
        self.department_quality_assurance = (
            By.XPATH, "//span[@id='select2-filter-by-department-container' and contains(text(), 'Quality Assurance')]"
        )
        self.location_dropdown = (By.XPATH, "//span[@id='select2-filter-by-location-container']")
        self.location_results_container = (By.XPATH, "//ul[@id='select2-filter-by-location-results']")
        self.istanbul_turkiye_option = (
            By.XPATH, "//*[@id='select2-filter-by-location-results']/li[contains(text(), 'Istanbul, Turkiye')]"
        )
        self.job_list = (By.CLASS_NAME, "position-list-item")
        self.job_titles = (By.XPATH, "//*[@id='jobs-list']/div/div/p")
        self.job_departments = (By.XPATH, "//*[@id='jobs-list']/div/div/span")
        self.job_locations = (By.XPATH, "//*[@id='jobs-list']/div/div/div")
        self.view_role_buttons = (By.XPATH, "//a[contains(text(), 'View Role')]")

    def go_to_qa_careers(self):
        """Navigate to the QA career page and close the cookie pop-up."""
        self.driver.get("https://useinsider.com/careers/quality-assurance/")
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.qa_jobs_button))

        try:
            cookie_button = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id='wt-cli-accept-all-btn']"))
            )
            cookie_button.click()
        except Exception:
            pass  # Continue if the cookie pop-up does not appear

        time.sleep(3)

    def click_qa_jobs(self):
        """Click on the 'See all QA jobs' button."""
        wait = WebDriverWait(self.driver, 20)
        qa_jobs_button = wait.until(EC.element_to_be_clickable(self.qa_jobs_button))
        qa_jobs_button.click()

    def filter_jobs(self):
        """Apply the location filter, ensuring that 'Quality Assurance' is selected first."""
        wait = WebDriverWait(self.driver, 30)
        wait.until(EC.presence_of_element_located(self.department_quality_assurance))

        location_dropdown = wait.until(EC.element_to_be_clickable(self.location_dropdown))
        location_dropdown.click()

        wait.until(EC.presence_of_element_located(self.location_results_container))
        istanbul_option = wait.until(EC.element_to_be_clickable(self.istanbul_turkiye_option))
        istanbul_option.click()

        # Wait for the page to load filtered job listings
        WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located(self.job_list))

    def check_job_list(self):
        """Verify that job listings are displayed and contain the correct information."""
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_all_elements_located(self.job_list))

        jobs = self.driver.find_elements(*self.job_list)
        soft_assert(len(jobs) > 0, "ERROR: No job listings were displayed!", self.errors, self.driver, "job_list")

        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", jobs[0])
        time.sleep(2)

        job_titles = self.driver.find_elements(*self.job_titles)
        job_departments = self.driver.find_elements(*self.job_departments)
        job_locations = self.driver.find_elements(*self.job_locations)

        for i in range(len(job_titles)):
            title_text = job_titles[i].text.strip()
            department_text = job_departments[i].text.strip()
            location_text = job_locations[i].text.strip()

            soft_assert("Quality Assurance" in title_text, f"Incorrect title: {title_text}", self.errors, self.driver, f"title_{i}")
            soft_assert(department_text == "Quality Assurance", f"Incorrect department: Expected 'Quality Assurance', Found: {department_text}", self.errors, self.driver, f"department_{i}")
            soft_assert(location_text == "Istanbul, Turkiye", f"Incorrect location: Expected 'Istanbul, Turkiye', Found: {location_text}", self.errors, self.driver, f"location_{i}")

        if self.errors:
            print("\nTest finished with errors:")
            for error in self.errors:
                print(f"  - {error}")

    def click_view_role(self):
        """Click the 'View Role' button to go to the application form and check the redirection."""
        wait = WebDriverWait(self.driver, 10)
        view_role_buttons = wait.until(EC.presence_of_all_elements_located(self.view_role_buttons))

        view_role_buttons[0].click()
        time.sleep(5)

        all_tabs = self.driver.window_handles
        self.driver.switch_to.window(all_tabs[-1])

        current_url = self.driver.current_url
        soft_assert("lever.co" in current_url, f"The page did not redirect to the application form! Current URL: {current_url}", self.errors, self.driver, "lever_redirect")
