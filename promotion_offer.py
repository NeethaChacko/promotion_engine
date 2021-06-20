import string
from dataclasses import dataclass


@dataclass
class Promotion(object):
    promotion_code: string
    product_name: string
    product_quantity: int
    promotion_discount: float

    def __init__(self, promotion_code, product_name, product_quantity, promotion_discount):
        self.promotion_code = promotion_code
        self.product_name = product_name
        self.product_quantity = product_quantity
        self.promotion_discount = promotion_discount

