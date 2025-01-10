import time

import pytest
from selenium.webdriver.common.by import By


class TestNegativeScenarios:

    @pytest.mark.login
    @pytest.mark.negative
    @pytest.mark.parametrize("username, password, expected_text",
                             [("incorrectUser", "Password123", "Your username is invalid!"),
                              ("student", "incorrect_password", "Your password is invalid!")])
    # enables parametrization of arguments for the function

    def test_negative_login(self, driver, username, password, expected_text):
        # Go to webpage
        driver.get("https://practicetestautomation.com/practice-test-login/")

        # Type username incorrectUser into Username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys(username)
        # username_locator.send_keys("student")

        # Type password Password123 into Password field
        password_locator = driver.find_element(By.ID, "password")
        password_locator.send_keys(password)

        # Push Submit button
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()
        time.sleep(2)

        # Verify error message is displayed

        # text_on_page = driver.find_element(By.XPATH, "//*[@text = 'Your username is invalid!']")
        element_with_text = driver.find_element(By.ID, "error")
        driver.execute_script("arguments[0].scrollIntoView();", element_with_text)
        assert element_with_text.is_displayed(), "Error message is not displayed, but it should be"

        # Verify error message text is Your username is invalid!
        text = element_with_text.text
        assert text == expected_text, "Error message is not expected"


def test_negative_username(self, driver):
    # Go to webpage
    driver.get("https://practicetestautomation.com/practice-test-login/")

    # Type username incorrectUser into Username field
    username_locator = driver.find_element(By.ID, "username")
    username_locator.send_keys("incorrectUser")
    # username_locator.send_keys("student")

    # Type password Password123 into Password field
    password_locator = driver.find_element(By.ID, "password")
    password_locator.send_keys("Password123")

    # Push Submit button
    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()
    time.sleep(2)

    # Verify error message is displayed

    # text_on_page = driver.find_element(By.XPATH, "//*[@text = 'Your username is invalid!']")
    element_with_text = driver.find_element(By.XPATH, "//*[contains(text(), 'Your username is invalid!')]")
    driver.execute_script("arguments[0].scrollIntoView();", element_with_text)
    assert element_with_text.is_displayed(), "Error message is not disaplyed, but it should be"

    # Verify error message text is Your username is invalid!
    expected_text = "Your username is invalid!"
    assert expected_text == element_with_text.text, "Error message is not expected"


def test_negative_password(self, driver):
    # Go to webpage
    driver.get("https://practicetestautomation.com/practice-test-login/")

    # Type username student into Username field
    username_locator = driver.find_element(By.ID, "username")
    username_locator.send_keys("student")

    # Type password incorrect_password into Password field
    password_locator = driver.find_element(By.ID, "password")
    password_locator.send_keys("incorrect_password")

    # Push Submit button
    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()
    time.sleep(2)

    # Verify error message is displayed
    element_with_text = driver.find_element(By.XPATH, "//*[contains(text(), 'Your password is invalid!')]")
    driver.execute_script("arguments[0].scrollIntoView();", element_with_text)
    assert element_with_text.is_displayed(), "Error message is not disaplyed, but it should be"

    # Verify error message text is Your username is invalid!
    expected_text = "Your password is invalid!"
    assert expected_text == element_with_text.text, "Error message is not expected"
