from selenium.webdriver.common.by import By
from pageObjects.ContactPage import ContactPage


class HomePage:

    def __init__(self,driver):
        self.driver = driver

    contact = (By.LINK_TEXT,"Contact")

    def user_contact(self):
       self.driver.find_element(*HomePage.contact).click()
       contactPage = ContactPage(self.driver)
       return contactPage