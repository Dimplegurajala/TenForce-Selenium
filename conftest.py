import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def driver():

    is_ci = os.getenv('CI', 'false').lower()=='true'
    
    # Setup Chrome Options
    options = Options()
    if is_ci:
         options.add_argument("--headless=new") #headless for github integration
         options.add_argument("--no-sandbox")
         options.add_argument("--disable-dev-shm-usage")
         options.add_argument("--start-maximized") # Handle maximizing here
         options.add_argument("--disable-gpu")
    else:
         print("\n [Info] Local environment detected- Running headaed mode for review")
         
    
    # Initialize Driver
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    
    # Yield driver to the test
    yield driver
    
    # Teardown: Close browser after test
    driver.quit()