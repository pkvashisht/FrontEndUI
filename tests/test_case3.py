import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.CartCheckoutPage import CartCheckoutPage
from pageObjects.ShopPage import ShopPage
from utilities.BaseClass import BaseClass


class TestThree(BaseClass):
    def test_case3(self):
        log = self.getLogger()
        shopPage = ShopPage(self.driver)
        #self.driver.find_element(By.LINK_TEXT,"Shop").click()
        shopPage.shopItems().click()
        #add_stuffedFrogs = self.driver.find_element(By.XPATH,"//li[@id='product-2']/div/p/a")
        log.info("Customer adding 2 Stuffed Frog, 5 Fluffy Bunny, 3 Valentine Bear to the cart!")

        add_stuffedFrogs = shopPage.add_frogIntoCart()
        for i in range(2):
            add_stuffedFrogs.click()

        add_fluffyBunny = shopPage.add_bunnyIntoCart()
        #add_fluffyBunny = self.driver.find_element(By.XPATH,"//li[@id='product-4']/div/p/a")
        for i in range(5):
            add_fluffyBunny.click()

        self.driver.execute_script("window.scrollBy(0,600)")

        add_valentineBeer = shopPage.add_bearIntoCart()
        #add_valentineBeer = self.driver.find_element(By.XPATH,"//li[@id='product-7']/div/p/a")
        for i in range(3):
            add_valentineBeer.click()

        cart_checkoutPage = CartCheckoutPage(self.driver)
        cart_checkoutPage.cart_button().click()
        #self.driver.find_element(By.ID,"nav-cart").click()
        #frog_price = float(self.driver.find_element(By.CSS_SELECTOR,"tbody tr:nth-child(1) td:nth-child(2)").text.strip("$"))
        #frog_subtotal = float(self.driver.find_element(By.CSS_SELECTOR,"tbody tr:nth-child(1) td:nth-child(4)").text.strip("$"))

        frog_price = float(cart_checkoutPage.frogPrice().text.strip("$"))
        frog_subtotal = float(cart_checkoutPage.frogSubtotal().text.strip("$"))
        assert frog_subtotal == frog_price * 2
        log.info(f"Stuffed Frog price is: {frog_price}, Subtotal is: {frog_subtotal}")
        # bunny_price = float(self.driver.find_element(By.CSS_SELECTOR,"tbody tr:nth-child(2) td:nth-child(2)").text.strip("$"))
        # bunny_subtotal = float(self.driver.find_element(By.CSS_SELECTOR,"tbody tr:nth-child(2) td:nth-child(4)").text.strip("$"))

        bunny_price = float(cart_checkoutPage.bunnyPrice().text.strip("$"))
        bunny_subtotal = float(cart_checkoutPage.bunnySubtotal().text.strip("$"))

        assert bunny_subtotal == bunny_price * 5
        log.info(f"Fluffy Bunny price is: {bunny_price}, Subtotal is: {bunny_subtotal}")
        # bear_price = float(self.driver.find_element(By.CSS_SELECTOR,"tbody tr:nth-child(3) td:nth-child(2)").text.strip("$"))
        # bear_subtotal = float(self.driver.find_element(By.CSS_SELECTOR,"tbody tr:nth-child(3) td:nth-child(4)").text.strip("$"))

        bear_price = float(cart_checkoutPage.bearPrice().text.strip("$"))
        bear_subtotal = float(cart_checkoutPage.bearSubtotal().text.strip("$"))

        assert bear_subtotal == bear_price * 3
        log.info(f"Valentine Bear price is: {bunny_price}, Subtotal is: {bunny_subtotal}")
        expected_total = (frog_subtotal + bunny_subtotal + bear_subtotal)
        #cart_total = (self.driver.find_element(By.CSS_SELECTOR,"strong[class='total ng-binding']").text)
        cart_total = cart_checkoutPage.cartTotal().text

        total_price = cart_total.split(":")[1].strip()

        assert expected_total == float(total_price)

        log.info(f"Verified that total: {total_price} = sum(sub totals):{expected_total}")

