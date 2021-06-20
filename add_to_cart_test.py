import unittest

from add_to_cart import Cart
from product_catalog import Product


class AddToCartTestCase(unittest.TestCase):
    def test_empty_cart(self):
        cart = Cart([])
        self.assertEqual(cart.calculate_total_price(), 0)

    def test_single_item_total(self):
        cart = Cart([Product("A", 50.0, 1)])
        self.assertEqual(cart.calculate_total_price(), 50)

    def test_single_item_multiple_quantity(self):
        cart = Cart([Product('A', 50.0, 2)])
        self.assertEqual(cart.calculate_total_price(), 100)
        cart = Cart([Product('C', 20.0, 3)])
        self.assertEqual(cart.calculate_total_price(), 60)
        cart = Cart([Product('D', 15.0, 2)])
        self.assertEqual(cart.calculate_total_price(), 30)

if __name__ == '__main__':
    unittest.main()
