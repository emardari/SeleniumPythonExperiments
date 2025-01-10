from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec, wait

from page_objects.base_page import BasePage


class LoginPage(BasePage):
    __url = "https://practicetestautomation.com/practice-test-login/"
    __username_field = (By.ID, "username")
    __password_field = (By.NAME, "password")
    __submit_button = (By.XPATH, "//button[@id='submit']")

    def __init__(self, driver: WebDriver):
        super().__init__()
        #self._driver = driver

    def open(self):
        super().open_url(self.__url)

    def execute_login(self, username: str, password: str):
        super()._type(self.__username_field, username)
        super()._type(self.__password_field, password)
        super()._click(self.__submit_button)

        # wait = WebDriverWait(self._driver, 10)
        # Type username student into Username field
        # wait.until(ec.visibility_of_element_located(self.__username_field))
        # self._driver.find_element(self.__username_field).send_keys()

        # Type password Password123 into Password field
        # wait.until(ec.visibility_of_element_located(self.__password_field))
        # self._driver.find_element(self.__password_field).send_keys()

        # Push Submit button
        # wait.until(ec.visibility_of_element_located(self.__submit_button))
        # self._driver.find_element(self.__submit_button).click()
