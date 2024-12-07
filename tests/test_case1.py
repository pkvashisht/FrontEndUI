from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass

class TestOne(BaseClass):
    def test_case1(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        contactPage = homePage.user_contact()
        contactPage.user_Submit().click()
        log.info("Verify error messages")
        error1 = contactPage.error_mesg1().text
        log.info(error1)
        assert error1 == "Forename is required"
        error2 = contactPage.error_mesg2().text
        log.info(error2)
        assert error2 == "Email is required"
        error3 = contactPage.error_mesg3().text
        log.info(error3)
        assert error3 == "Message is required"
        log.info("Populating mandatory fields")
        contactPage.add_userName().send_keys("parveen")
        contactPage.add_userEmail().send_keys("pkvashisht93@gmail.com")
        contactPage.add_msg().send_keys("Hi this is my first Test case")
        contactPage.user_Submit().click()
        wait = WebDriverWait(self.driver,30)
        wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,"div[class='alert alert-success']")))
        feedbackSubmit = contactPage.feedback_confirmation_msg().text
        assert feedbackSubmit == "Thanks parveen, we appreciate your feedback."
        log.info("Validated error has gone and Feedback submitted successfully!")
