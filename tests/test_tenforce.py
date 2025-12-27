import pytest
from pages.career_page import CareerPage

def test_tenforce_navigation(driver):
    print("\n--- STARTING TEST ---")
    navigation = CareerPage(driver)
    
    # 1. Open Tenforce Homepage
    driver.get("https://www.tenforce.com")
    print("[SUCCESS] Homepage loaded.")

    # 2. Open Careers
    navigation.navigating_to_careers()
    
    # 3. navigate to Life at Tenforce 
    navigation.navigating_to_life_at_tenforce()
    
    # 4. Open "Life of two interns" article and scroll
    navigation.open_and_scroll_intern_article()
    
    # 5. Go back to Job openings
    navigation.return_to_job_openings()
    
    # 6.Assertion
    actual_text = navigation.get_cv_text_assertion()
    # Assert on the stored variable
    assert "Feel free to send your CV to" in actual_text
    print("\n[SUCCESS] Final Assertion Passed: CV text verified.")