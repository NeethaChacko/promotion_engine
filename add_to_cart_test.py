import unittest
from dataclasses import dataclass
from typing import List


@dataclass
class Cart:
    items: List

    @staticmethod
    def calculate_total_price():
        return 0


class AddToCartTestCase(unittest.TestCase):
    def test_empty_cart(self):
        cart = Cart([])
        self.assertEqual(cart.calculate_total_price(), 0)


if __name__ == '__main__':
    unittest.main()
