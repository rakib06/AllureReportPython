from allure_commons.types import AttachmentType
from selenium import webdriver
import allure
import pytest
from selenium.webdriver.common.by import  By


@allure.severity(allure.severity_level.NORMAL)
class TestDemo:

    @allure.severity(allure.severity_level.MINOR)
    def test_logo(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        status = self.driver.find_element(By.XPATH, '//*[@id="divLogo"]/img').is_displayed()
        self.driver.close()
        if status:
            assert True
        else:
            assert False

    @allure.severity(allure.severity_level.NORMAL)
    def test_list_employees(self):
        pytest.skip("Skipping Test.. Later I will implement")

    @allure.severity(allure.severity_level.CRITICAL)
    def test_login(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element(By.ID, "txtUsername").send_keys("Admin")
        self.driver.find_element(By.ID, "txtPassword").send_keys("admin123")
        self.driver.find_element(By.ID, 'btnLogin').click()
        actual_title = self.driver.title
        self.driver.close()
        if actual_title == "OrangeHRM123": # Expected Title
            allure.attach(self.driver.get_screenshot_as_png(), "Test Login Screen",\
                          attachment_type=AttachmentType.PNG)
            assert True
        else:
            assert False


#  pytest -v -s .\allure-report-demo\test_demo.py
#  pytest -v -s --alluredir=".\allure-report-demo\reports" .\allure-report-demo\test_demo.py