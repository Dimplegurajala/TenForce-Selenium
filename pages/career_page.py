from selenium.webdriver.common.by import By 
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class CareerPage(BasePage):

    # Locators to perform all navigations-
    COOKIE_BTN = (By.XPATH, "//button[contains(normalize-space(), 'I Agree')]")
    ABOUT_US_MENU = (By.XPATH, "//span[contains(normalize-space(), 'About Us')]")
    
    CAREER_LINK = (By.XPATH, "//a[contains(@href, '/career')]")
    LIFE_AT_TENFORCE_TAB = (By.XPATH, "//a[contains(normalize-space(), 'Life at TenForce')]")
    JOB_OPENINGS_TAB = (By.XPATH, "//a[contains(normalize-space(), 'Job Openings')]")
    INTERN_ARTICLE = (By.XPATH, "//span[contains(normalize-space(), 'Life of two interns')]")
    CV_MESSAGE_TEXT= (By.XPATH, "//*[text()[contains(.,'Feel free to send your CV to')]]")
   
    def navigating_to_careers(self):
        print("Checking for Cookie Banner...")
        try:
            if self.driver.find_elements(*self.COOKIE_BTN):
                self.click(self.COOKIE_BTN)
                print("[SUCCESS] Cookie Banner Accepted.")
        except:
            print("[INFO] Cookie Banner not found (skippable).")
        self.hover_and_click(self.ABOUT_US_MENU, self.CAREER_LINK)
        print("[SUCCESS] Navigated to Career page.")

    def navigating_to_life_at_tenforce(self):
        print("Clicking 'Life at TenForce' tab...")
        self._js_click(self.LIFE_AT_TENFORCE_TAB)
        # Wait for the article list to load
        self.wait.until(EC.presence_of_element_located(self.INTERN_ARTICLE))
        print("[SUCCESS] 'Life at TenForce' section is loaded.")

    def open_and_scroll_intern_article(self):
        print("Opening 'Life of two interns' article...") 
        self.scroll_and_click(self.INTERN_ARTICLE)
        self.wait.until(EC.url_contains("interns"))
        print("[SUCCESS] Article opened. URL verified.")
        
        print("Scrolling to bottom of article...")
        self.scroll_to_bottom()
        print("[SUCCESS] Scrolled to the bottom of the article.")
        
    def return_to_job_openings(self):
        print("Returning to main Career Page URL...")
        self.driver.get("https://www.tenforce.com/career")
        print(" Clicking 'Job Openings' tab...")
        self.scroll_and_click(self.JOB_OPENINGS_TAB)
        print("[SUCCESS] Returned to Job Openings tab.")

    def get_cv_text_assertion(self):
        print("[ACTION] Extracting CV Message text...")
        text = self.get_text(self.CV_MESSAGE_TEXT)
        print(f"[SUCCESS] Extracted text: '{text}'")
        return text