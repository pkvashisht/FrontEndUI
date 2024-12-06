from selenium.webdriver.common.by import By


class CartCheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    cart = (By.ID,"nav-cart")

    frgPrice = (By.CSS_SELECTOR,"tbody tr:nth-child(1) td:nth-child(2)")
    frgSubtotal = (By.CSS_SELECTOR,"tbody tr:nth-child(1) td:nth-child(4)")

    bnyPrice = (By.CSS_SELECTOR,"tbody tr:nth-child(2) td:nth-child(2)")
    bnySubtotal = (By.CSS_SELECTOR,"tbody tr:nth-child(2) td:nth-child(4)")

    brPrice = (By.CSS_SELECTOR,"tbody tr:nth-child(3) td:nth-child(2)")
    brSubtotal = (By.CSS_SELECTOR,"tbody tr:nth-child(3) td:nth-child(4)")

    total = (By.CSS_SELECTOR,"strong[class='total ng-binding']")



    def cart_button(self):
        return self.driver.find_element(*CartCheckoutPage.cart)
    def frogPrice(self):
        return self.driver.find_element(*CartCheckoutPage.frgPrice)

    def frogSubtotal(self):
        return self.driver.find_element(*CartCheckoutPage.frgSubtotal)

    def bunnyPrice(self):
        return self.driver.find_element(*CartCheckoutPage.bnyPrice)

    def bunnySubtotal(self):
        return self.driver.find_element(*CartCheckoutPage.bnySubtotal)

    def bearPrice(self):
        return self.driver.find_element(*CartCheckoutPage.brPrice)

    def bearSubtotal(self):
        return self.driver.find_element(*CartCheckoutPage.brSubtotal)


    def cartTotal(self):
        return self.driver.find_element(*CartCheckoutPage.total)
