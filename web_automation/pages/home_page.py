from selenium.webdriver.common.by import By

class HomePage:
    """ Insider ana sayfa işlemleri """
    
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://useinsider.com/"
        self.company_menu = (By.XPATH, "//a[contains(text(),'Company')]")
        self.careers_link = (By.XPATH, "//a[contains(text(),'Careers')]")

    def open_home_page(self):
        """ Insider ana sayfasını aç """
        self.driver.get(self.url)

    def go_to_careers_page(self):
        """ 'Company' menüsünden 'Careers' sayfasına git """
        self.driver.find_element(*self.company_menu).click()
        self.driver.find_element(*self.careers_link).click()
 
