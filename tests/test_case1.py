import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.ContactPage import ContactPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


#@pytest.mark.usefixtures("setup")
class TestOne(BaseClass):
    def test_case1(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        contactPage = homePage.user_contact()
        #self.driver.find_element(By.LINK_TEXT,"Contact").click()
        #contactPage = ContactPage(self.driver)
        contactPage.user_Submit().click()
        #self.driver.find_element(By.LINK_TEXT,"Submit").click()
        #error1 = self.driver.find_element(By.ID,"forename-err").text
        log.info("Verify error messages")
        error1 = contactPage.error_mesg1().text
        log.info(error1)
        assert error1 == "Forename is required"
        error2 = contactPage.error_mesg2().text
        log.info(error2)
        #error2 = self.driver.find_element(By.ID,"email-err").text
        assert error2 == "Email is required"

        #error3 = self.driver.find_element(By.ID,"message-err").text
        error3 = contactPage.error_mesg3().text
        log.info(error3)
        assert error3 == "Message is required"
        log.info("Populating mandatory fields")
        #self.driver.find_element(By.ID,"forename").send_keys("parveen")
        contactPage.add_userName().send_keys("parveen")
        #self.driver.find_element(By.ID,"email").send_keys("pkvashisht93@gmail.com")
        contactPage.add_userEmail().send_keys("pkvashisht93@gmail.com")
        #self.driver.find_element(By.ID,"message").send_keys("Hi this is my first Test case")
        contactPage.add_msg().send_keys("Hi this is my first Test case")
        #self.driver.find_element(By.LINK_TEXT,"Submit").click()
        contactPage.user_Submit().click()
        wait = WebDriverWait(self.driver,30)
        wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,"div[class='alert alert-success']")))

        #feedbackSubmit = self.driver.find_element(By.CSS_SELECTOR,"div[class='alert alert-success']").text

        feedbackSubmit = contactPage.feedback_confirmation_msg().text
        assert feedbackSubmit == "Thanks parveen, we appreciate your feedback."
        log.info("Validated error has gone and Feedback submitted successfully!")
