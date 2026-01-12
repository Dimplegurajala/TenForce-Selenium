from selenium.webdriver.common.by import By 
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class CareerPage(BasePage):
    # Locators
    COOKIE_BTN    = (By.CSS_SELECTOR, "button.gdpr-agreement")
    ABOUT_US_MENU = (By.CSS_SELECTOR, "nav span.is-permalink")
    CAREER_LINK   = (By.CSS_SELECTOR, "ul.tf-navbar__inner-nav a[href='/career']")
    
    LIFE_AT_TENFORCE_TAB = (By.CSS_SELECTOR, "a[data-type='people']")
    JOB_OPENINGS_TAB     = (By.CSS_SELECTOR, "a[data-type='job']")
    
    INTERN_ARTICLE       = (By.XPATH, "//span[contains(text(), 'Life of two interns')]")
    CV_MESSAGE_TEXT      = (By.XPATH, "//*[contains(text(), 'Feel free to send your CV')]")

    def navigating_to_careers(self):
        if self.driver.find_elements(*self.COOKIE_BTN):
            self.click(self.COOKIE_BTN)
        
        # Ensures the viewport is at 0,0 for clean hover interaction
        self.driver.execute_script("window.scrollTo(0, 0);")
        
        # hover_and_click already contains its own explicit wait
        self.hover_and_click(self.ABOUT_US_MENU, self.CAREER_LINK)

    def navigating_to_life_at_tenforce(self):
        # Dynamic: Wait for the URL to change first
        self.wait.until(EC.url_contains("/career"))
        
        # Dynamic: Wait for the tab to be interactable instead of sleeping
        self.wait.until(EC.element_to_be_clickable(self.LIFE_AT_TENFORCE_TAB))
        self.scroll_and_click(self.LIFE_AT_TENFORCE_TAB)
        
        self.wait.until(EC.visibility_of_element_located(self.INTERN_ARTICLE))

    def open_and_scroll_intern_article(self):
        self.scroll_and_click(self.INTERN_ARTICLE)
        self.wait.until(EC.url_contains("interns"))
        self.scroll_to_bottom()
        
    def return_to_job_openings(self):
        #Bypasses SPA state issues with a direct GET and state-sync.
        self.driver.get("https://www.tenforce.com/career")
        # Ensuring the job tab is ready before clicking
        self.wait.until(EC.element_to_be_clickable(self.JOB_OPENINGS_TAB))
        self.scroll_and_click(self.JOB_OPENINGS_TAB)

    def get_cv_text_assertion(self):
        return self.get_text(self.CV_MESSAGE_TEXT)