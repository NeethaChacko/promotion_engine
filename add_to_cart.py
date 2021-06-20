import string
from dataclasses import dataclass
from typing import List

from product_catalog import Product


@dataclass
class Cart(object):
    items: List[Product]

    def calculate_total_price(self):
        if len(self.items) > 0:
            return self.items[0].unit_price
        return 0


