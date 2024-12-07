from pageObjects.CartCheckoutPage import CartCheckoutPage
from pageObjects.ShopPage import ShopPage
from utilities.BaseClass import BaseClass


class TestThree(BaseClass):

    def test_case3(self):

        log = self.getLogger()
        shopPage = ShopPage(self.driver)
        shopPage.shopItems().click()
        log.info("Customer adding 2 Stuffed Frog, 5 Fluffy Bunny, 3 Valentine Bear to the cart!")
        add_stuffedFrogs = shopPage.add_frogIntoCart()
        for i in range(2):
            add_stuffedFrogs.click()

        add_fluffyBunny = shopPage.add_bunnyIntoCart()
        for i in range(5):
            add_fluffyBunny.click()

        #self.driver.execute_script("window.scrollBy(0,600)")
        add_valentineBeer = shopPage.add_bearIntoCart()
        for i in range(3):
            add_valentineBeer.click()

        cart_checkoutPage = CartCheckoutPage(self.driver)
        cart_checkoutPage.cart_button().click()

        frog_price = float(cart_checkoutPage.frogPrice().text.strip("$"))
        frog_subtotal = float(cart_checkoutPage.frogSubtotal().text.strip("$"))
        assert frog_subtotal == frog_price * 2
        log.info(f"Stuffed Frog price is: {frog_price}, Subtotal is: {frog_subtotal}")

        bunny_price = float(cart_checkoutPage.bunnyPrice().text.strip("$"))
        bunny_subtotal = float(cart_checkoutPage.bunnySubtotal().text.strip("$"))
        assert bunny_subtotal == bunny_price * 5
        log.info(f"Fluffy Bunny price is: {bunny_price}, Subtotal is: {bunny_subtotal}")

        bear_price = float(cart_checkoutPage.bearPrice().text.strip("$"))
        bear_subtotal = float(cart_checkoutPage.bearSubtotal().text.strip("$"))
        assert bear_subtotal == bear_price * 3
        log.info(f"Valentine Bear price is: {bunny_price}, Subtotal is: {bunny_subtotal}")

        expected_total = (frog_subtotal + bunny_subtotal + bear_subtotal)
        cart_total = cart_checkoutPage.cartTotal().text
        total_price = cart_total.split(":")[1].strip()
        assert expected_total == float(total_price)

        log.info(f"Verified that total: {total_price} = sum(sub totals):{expected_total}")

