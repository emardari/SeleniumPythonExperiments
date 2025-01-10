from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.base_page import BasePage


class LoggedInSuccessfullyPage(BasePage):
    url = "https://practicetestautomation.com/logged-in-successfully/"
    __header_locator = (By.TAG_NAME, "h1")
    __log_out_button_locator = (By.LINK_TEXT, "Log out")

    def __init__(self, driver: WebDriver):
        super().__init__()
        # self._driver = driver

    # @property
    # def current_url(self) -> str:
      #   actual_url = self._driver.current_url
        # return actual_url

    # or return self._driver.current_url

    @property
    def expected_url(self) -> str:
        return self._url

    @property
    def header(self) -> str:
        return super()._get_text(self.__header_locator)
       # return self._driver.find_element(self.__header_locator).text

    def is_log_out_button_displayed(self) -> bool:
        return super().is_displayed(self.__log_out_button_locator)
        # return self._driver.find_element(self.__log_out_button_locator).is_displayed()
