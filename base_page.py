from selenium.common import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def find(self, locator) -> WebElement:
        self.wait_until_element_is_visible(10, locator)
        return self.driver.find_element(*locator)

    def enter(self, locator, text: str, time: int = 10):
        self.wait_until_element_is_visible(locator, time)
        self.find(locator).send_keys(text)

    def click(self, locator):
        self.wait_until_element_is_visible(10, locator)
        self.find(locator).click()

    def wait_until_element_is_visible(self, time, locator):
        wait = WebDriverWait(self.driver, time)
        wait.until(EC.visibility_of_element_located(locator))

    @property
    def current_url(self) -> str:
        return self.driver.current_url

    def get_text(self, locator):
        self.wait_until_element_is_visible(10, locator)
        return self.find(locator).text

    def is_displayed(self, locator) -> bool:
        try:
            return self.find(locator).is_displayed()
        except NoSuchElementException:
            return False

