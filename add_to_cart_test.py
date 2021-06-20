import unittest

from add_to_cart import Cart
from product_catalog import Product


class AddToCartTestCase(unittest.TestCase):
    def test_empty_cart(self):
        cart = Cart()
        self.assertEqual(cart.calculate_total_price(), 0)

    def test_single_item_total(self):
        product = Product("A", 50.0)
        cart = Cart()
        cart.add_item_to_cart(product, 1)
        self.assertEqual(cart.calculate_total_price(), 50)
        product = Product("B", 30.0)
        cart = Cart()
        cart.add_item_to_cart(product, 1)
        self.assertEqual(cart.calculate_total_price(), 30)
        product = Product("C", 20.0)
        cart = Cart()
        cart.add_item_to_cart(product, 1)
        self.assertEqual(cart.calculate_total_price(), 20)
        product = Product("D", 15.0)
        cart = Cart()
        cart.add_item_to_cart(product, 1)
        self.assertEqual(cart.calculate_total_price(), 15)

    def test_single_item_multiple_quantity(self):
        product = Product("A", 50.0)
        cart = Cart()
        cart.add_item_to_cart(product, 2)
        self.assertEqual(cart.calculate_total_price(), 100)

        product = Product("C", 20.0)
        cart = Cart()
        cart.add_item_to_cart(product, 2)
        self.assertEqual(cart.calculate_total_price(), 40)

        product = Product("D", 15.0)
        cart = Cart()
        cart.add_item_to_cart(product, 2)
        self.assertEqual(cart.calculate_total_price(), 30)

    def test_multiple_item_single_quantity(self):
        # Scenario 1:  (A(1) + B(1) + C(1) in cart
        product = Product("A", 50.0)
        cart = Cart()
        cart.add_item_to_cart(product, 1)
        product = Product("B", 30.0)
        cart.add_item_to_cart(product, 1)
        product = Product("C", 20.0)
        cart.add_item_to_cart(product, 1)
        self.assertEqual(cart.calculate_total_price(), 100)


if __name__ == '__main__':
    unittest.main()
