# pages/base_page.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
import time

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)  # Increased timeout from 10 to 15 slightly for stability

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def _scroll_to_center(self, element):
        # Scrolls element to center - to see everything accross the page
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        time.sleep(0.5)

    def click(self, locator):
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
        except ElementClickInterceptedException:
            # Fallback: Scroll to center and retrying standard click
            element = self.find(locator)
            self._scroll_to_center(element)
            element.click()

    def _js_click(self, locator):
        element = self.find(locator)
        self.driver.execute_script("arguments[0].click();", element)

    def hover_and_click(self, hover_locator, click_locator):
        try:
            hover_element = self.find(hover_locator)
            self._scroll_to_center(hover_element)

            actions = ActionChains(self.driver)
            actions.move_to_element(hover_element).perform()

            self.wait.until(EC.visibility_of_element_located(click_locator))
            
            click_el = self.find(click_locator)
            actions.move_to_element(click_el).click().perform()
        except Exception as e:
            self._js_click(click_locator)

    def scroll_and_click(self, locator):
        try:
            #Find and Scroll and center
            element = self.find(locator)
            self._scroll_to_center(element)
            
            # Waiting for it to be clickable (not just visible)
            self.wait.until(EC.element_to_be_clickable(locator))
            
            # Standard Click for elements which are not related to ActionChains
            element.click()
            
        except Exception:
            self._js_click(locator)

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def get_text(self, locator):
        element = self.find(locator)
        self._scroll_to_center(element)
        self.wait.until(EC.visibility_of_element_located(locator))
        return element.text.strip()