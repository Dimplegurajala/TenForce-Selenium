import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def driver():
    #Configuration - Chrome with CI/Headless support- Env aware
    is_ci = os.getenv('CI', 'false').lower() == 'true'
    options = Options()
    #Optimising testsuite for GitHub pipeline
    if is_ci:
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
    
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()