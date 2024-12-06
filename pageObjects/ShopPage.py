from selenium.webdriver.common.by import By
class ShopPage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.LINK_TEXT,"Shop")
    frog = (By.XPATH,"//li[@id='product-2']/div/p/a")
    bunny = (By.XPATH,"//li[@id='product-4']/div/p/a")
    bear = (By.XPATH,"//li[@id='product-7']/div/p/a")

    def shopItems(self):
        return self.driver.find_element(*ShopPage.shop)

    def add_frogIntoCart(self):
        return self.driver.find_element(*ShopPage.frog)

    def add_bunnyIntoCart(self):
        return self.driver.find_element(*ShopPage.bunny)

    def add_bearIntoCart(self):
        return self.driver.find_element(*ShopPage.bear)
