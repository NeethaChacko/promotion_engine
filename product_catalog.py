import string
from dataclasses import dataclass


@dataclass
class Product:
    product_name: string
    unit_price: float
    quantity: 1

    def __init__(self, product_name, unit_price, quantity):
        self.product_name = product_name
        self.unit_price = unit_price
        self.quantity = quantity
