from selenium.webdriver.common.by import By


class ContactPage:

    def __init__(self, driver):
        self.driver = driver

    submit_form = (By.LINK_TEXT,"Submit")
    error1 = (By.ID,"forename-err")
    error2 = (By.ID,"email-err")
    error3 = (By.ID,"message-err")
    name = (By.ID,"forename")
    email = (By.ID,"email")
    message = (By.ID,"message")
    ConfirmMsg = (By.CSS_SELECTOR,"div[class='alert alert-success']")

    def user_Submit(self):

        return self.driver.find_element(*ContactPage.submit_form)

    def error_mesg1(self):
        return self.driver.find_element(*ContactPage.error1)

    def error_mesg2(self):
        return self.driver.find_element(*ContactPage.error2)

    def error_mesg3(self):
        return self.driver.find_element(*ContactPage.error3)

    def add_userName(self):
        return self.driver.find_element(*ContactPage.name)

    def add_userEmail(self):
        return self.driver.find_element(*ContactPage.email)

    def add_msg(self):
        return self.driver.find_element(*ContactPage.message)

    def feedback_confirmation_msg(self):
        return self.driver.find_element(*ContactPage.ConfirmMsg)