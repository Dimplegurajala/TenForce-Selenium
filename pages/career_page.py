from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class CareerPage(BasePage):
    # Locators - used both CSS and XPATH
    COOKIE_BTN           = (By.CSS_SELECTOR, "button.gdpr-agreement")
    ABOUT_US_MENU        = (By.XPATH, "//span[contains(@class, 'is-permalink') and contains(text(), 'About Us')]")
    CAREER_LINK          = (By.CSS_SELECTOR, "a[href='/career']")
    LIFE_AT_TENFORCE_TAB = (By.CSS_SELECTOR, "a[data-type='people']")
    JOB_OPENINGS_TAB     = (By.CSS_SELECTOR, "a[data-type='job']")
    INTERN_ARTICLE       = (By.XPATH, "//span[contains(@class, 'is-link') and contains(text(), 'Life of two interns')]")
    CV_MESSAGE_TEXT      = (By.XPATH, "//span[contains(text(), 'Feel free to send your CV')]")

    def navigating_to_careers(self):
        try:
            self.click(self.COOKIE_BTN)
        except:
            pass
        self.hover_and_click(self.ABOUT_US_MENU, self.CAREER_LINK)

    def navigating_to_life_at_tenforce(self):
        self.wait.until(EC.url_contains("/career"))
        self.scroll_and_click(self.LIFE_AT_TENFORCE_TAB)
        self.wait.until(EC.visibility_of_element_located(self.INTERN_ARTICLE))

    def open_and_scroll_intern_article(self):
        self.scroll_and_click(self.INTERN_ARTICLE)
        self.wait.until(EC.url_contains("interns"))
        self.scroll_to_bottom()

    def return_to_job_openings(self):
        #driver.back() - was not working due to SPA nature of the Tenforce website
        self.driver.get("https://www.tenforce.com/career")
        self.scroll_and_click(self.JOB_OPENINGS_TAB)

    def get_cv_text_assertion(self):
        return self.get_text(self.CV_MESSAGE_TEXT)