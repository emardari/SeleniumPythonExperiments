from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec, wait


class TestExceptions:

    @pytest.mark.exceptiontests
    def test_no_such_element_exception(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Click Add button
        add_button = driver.find_element(By.XPATH, "//button[@id='add_btn']")
        add_button.click()

        wait = WebDriverWait(driver, 10)
        wait.until(ec.presence_of_element_located((By.XPATH, "//div[@id='row2']/input")))

        # Verify Row 2 input field is displayed
        row_two = driver.find_element(By.XPATH, "//div[@id='row2']/input")

        # or do it like this: row_two = wait.until(ec.presence_of_element_located((By.XPATH, "//div[@id='row2']/input")))
        # because in such a way we do not need to look for the element twice
        driver.execute_script("arguments[0].scrollIntoView();", row_two)
        assert row_two.is_displayed()

        # Row 2 doesn’t appear immediately. This test will fail with org.openqa.selenium.NoSuchElementException without proper wait
        # wait with Python: WebDriverWait(driver, timeout=3).until(some_condition)

    @pytest.mark.exceptiontests
    @pytest.mark.debug
    def test_element_not_interactable_exception(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Click Add button
        add_button = driver.find_element(By.XPATH, "//button[@id='add_btn']")
        add_button.click()

        # Wait for the second row to load
        wait = WebDriverWait(driver, 10)
        row_two = wait.until(ec.presence_of_element_located((By.XPATH, "//div[@id='row2']/input")))

        # Type text into the second input field
        row_two.send_keys("water")

        # Push Save button using locator By.name(“Save”)
        driver.find_element(By.XPATH, "//div[@id='row2']/button[@name='Save']").click()
        # save_button.click()

        # Verify text saved
        confirmation_element = driver.find_element(By.ID, "confirmation")
        confirmation_message = confirmation_element.text
        assert confirmation_message == "Row 2 was saved", "Confirmation message"

    @pytest.mark.exceptiontests
    @pytest.mark.debug
    def test_invalid_element_state_exception(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Clear input field
        edit_button = driver.find_element(By.XPATH, "//button[@id='edit_btn']")
        edit_button.click()

        row_one = driver.find_element(By.XPATH, "//div[@id='row1']/input")
        wait = WebDriverWait(driver, 5)
        wait.until(ec.element_to_be_clickable(row_one))
        row_one.clear()

        # Type text into the input field
        row_one.send_keys("Hello")

        # Push Save button
        save_button = driver.find_element(By.ID, "save_btn")
        save_button.click()

        # Verify text changed
        confirmation_element = wait.until(ec.visibility_of_element_located((By.ID, "confirmation")))
        confirmation_message = confirmation_element.text
        assert confirmation_message == "Row 1 was saved", "Confirmation message is not expected"

    @pytest.mark.exceptiontests
    @pytest.mark.debug
    def test_stale_element_reference_exception(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Find the instructions text element
        instructions_element = driver.find_element(By.ID, "instructions")
        assert instructions_element.is_displayed()

        # Push Add button
        add_button = driver.find_element(By.XPATH, "//button[@id='add_btn']")
        add_button.click()

        # Verify instruction text element is no longer displayed
        wait = WebDriverWait(driver, 10)
        assert wait.until(ec.invisibility_of_element_located((By.ID, "instructions")),
                          "Instruction message should not be displayed")
        # assert not instructions_element.is_displayed(), "Instruction message should not be displayed"

    @pytest.mark.exceptiontests
    @pytest.mark.debug
    def test_timeout_exception(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Click Add button
        add_button = driver.find_element(By.XPATH, "//button[@id='add_btn']")
        add_button.click()

        # Wait for 3 seconds for the second input field to be displayed
        wait = WebDriverWait(driver, 6)

        # Verify second input field is displayed
        assert wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@id='row2']/input")),
                          "Failed waiting for Row 2 to be visible")
