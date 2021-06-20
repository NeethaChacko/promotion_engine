import string
from dataclasses import dataclass
from functools import reduce
from typing import List

from product_catalog import Product


@dataclass
class Cart(object):
    prod_dict = {
        "items": List[Product],
        "quantity": 0
    }
    total_price = 0
    # items: List[Product]

    @staticmethod
    def add_item_to_cart(product_name, quantity):
        cart = Cart()
        cart.prod_dict["items"] = product_name
        cart.prod_dict["quantity"] = quantity

    def calculate_total_price(self):
        if bool(self.prod_dict):  # cart created
            # if any(d['items'] == Product for d in self.prod_dict) # cart not empty

            if len(self.prod_dict) > 0:  # MODIFY: check cart not empty condition
                self.total_price = (self.prod_dict["quantity"] * (self.prod_dict["items"]).unit_price)
                return self.total_price
            else:
                return 0  # to return 0 when cart is empty

        #for each_cart_item in self.prod_dict.values():
         #   self.total_price = each_cart_item["items"][1]
          #  return self.total_price
            # for prod in each_cart_item:




