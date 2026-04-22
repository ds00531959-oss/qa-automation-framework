from pages.login_page import LoginPage

def test_valid_login(driver):
    page = LoginPage(driver)
    page.open()
    page.login("standard_user", "secret_sauce")

    assert "inventory" in driver.current_url


def test_invalid_login(driver):
    page = LoginPage(driver)
    page.open()
    page.login("invalid_user", "wrong_pass")

    assert "Username and password do not match" in page.get_error()


def test_add_to_cart(driver):
    from pages.inventory_page import InventoryPage

    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver)
    inventory.add_product_to_cart()
    inventory.go_to_cart()

    assert "cart" in driver.current_url


def test_checkout_flow(driver):
    from pages.inventory_page import InventoryPage
    from pages.cart_page import CartPage
    from pages.checkout_page import CheckoutPage

    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver)
    inventory.add_product_to_cart()
    inventory.go_to_cart()

    cart = CartPage(driver)
    cart.click_checkout()

    checkout = CheckoutPage(driver)
    checkout.fill_details()
    checkout.continue_checkout()
    checkout.finish_checkout()

    assert "checkout-complete" in driver.current_url
