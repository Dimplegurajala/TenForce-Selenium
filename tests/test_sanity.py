import pytest

def test_launch_and_title(driver):
    
    # checking for browser health
    target_url = "https://www.tenforce.com/"
    driver.get(target_url)
    
    # a simple assertion of title on the page loaded
    expected_title= "TenForce"
    actual_title = driver.title
    
    assert expected_title in actual_title, f"Browser Health Check Failed! Expected '{expected_title}' in '{actual_title}'"