import string
from dataclasses import dataclass
from functools import reduce
from typing import List

from product_catalog import Product


@dataclass
class Cart(object):
    items: List[Product]

    def calculate_total_price(self):
        return reduce(lambda subtotal, product_catalog: subtotal + (product_catalog.unit_price
                                                                   * product_catalog.quantity), self.items, 0)

        return 0


