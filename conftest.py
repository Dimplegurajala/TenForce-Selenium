import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def driver():
    
    # Setup Chrome Options
    options = Options()
    options.add_argument("--headless=new") #headless for github integration
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--start-maximized") # Handle maximizing here
    options.add_argument("--disable-gpu")
    
    # Initialize Driver
    driver = webdriver.Chrome(options=options)
    
    # Yield driver to the test
    yield driver
    
    # Teardown: Close browser after test
    driver.quit()