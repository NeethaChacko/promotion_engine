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


if __name__ == '__main__':
    unittest.main()
