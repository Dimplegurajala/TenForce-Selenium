import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def scroll(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
         

    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def get_text(self, locator):
        element = self.find(locator)
        self.scroll(element)
        return element.text.strip()

    def hover_and_click(self, hover_locator, click_locator):
        try:
            hover_el = self.find(hover_locator)
            self.scroll(hover_el)
            actions = ActionChains(self.driver)
            actions.move_to_element(hover_el).perform()
            
            click_el = self.wait.until(EC.visibility_of_element_located(click_locator))
            actions.move_to_element(click_el).click().perform()
        except:
            self._js_click(click_locator)

    def scroll_and_click(self, locator):
        element = self.find(locator)
        self.scroll(element)
        try:
            self.wait.until(EC.element_to_be_clickable(locator)).click()
        except:
            self._js_click(locator)

    def _js_click(self, locator):
        element = self.find(locator)
        self.driver.execute_script("arguments[0].click();", element)

    