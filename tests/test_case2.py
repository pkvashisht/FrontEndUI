import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utilities.BaseClass import BaseClass

class TestTwo(BaseClass):
    def test_case2(self):
        self.driver.find_element(By.LINK_TEXT,"Contact").click()
        self.driver.find_element(By.ID,"forename").send_keys("parveen")
        self.driver.find_element(By.ID,"email").send_keys("pkvashisht93@gmail.com")
        self.driver.find_element(By.ID,"message").send_keys("Hi this is my first Test case")
        self.driver.find_element(By.LINK_TEXT,"Submit").click()

        wait = WebDriverWait(self.driver,30)
        wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,"div[class='alert alert-success']")))

        feedbackSubmit = self.driver.find_element(By.CSS_SELECTOR,"div[class='alert alert-success']").text

        assert feedbackSubmit == "Thanks parveen, we appreciate your feedback."

