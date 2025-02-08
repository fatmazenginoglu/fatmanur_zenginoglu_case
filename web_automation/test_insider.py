import pytest
from pages.home_page import HomePage
from pages.career_page import CareerPage

@pytest.mark.usefixtures("driver")
def test_insider_careers(driver):
    """Insider career page test scenario"""
    
    # **Home Page Operations**
    home = HomePage(driver)
    home.open_home_page()  # 1. Open the Insider homepage
    home.go_to_careers_page()  # 2. Navigate to the Careers page

    # **Career Page Operations**
    career = CareerPage(driver)

    # **Navigate directly to the QA career page**
    career.go_to_qa_careers()  

    # **Click on the 'See all QA jobs' button**
    career.click_qa_jobs()    
    
    # **Apply location and department filters**
    career.filter_jobs()
    
    # **Verify that the job listings are displayed**
    career.check_job_list()

    # **Verify that clicking the "View Role" button redirects to the application form**
    career.click_view_role() 
    
    print("✅ Test completed successfully!")
