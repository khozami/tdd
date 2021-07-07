"""
Module: Checkout
"""
from collections import defaultdict

class Checkout:
    """
    Checkout class:
    Mathods:
     - add_item_price
    """
    def __init__(self):
        """
        init items as an empty dictionary
        """
        self.items = defaultdict(lambda : 0)

    def add_item_price(self, item, price):
        """
        Add an item price
        """
        self.items[item] = price

    def add_item(self , item):
        """
        Add item without price
        """
        return self.items[item]

    def calculate_total(self):
        """
        Calculate and return total
        """
        return sum(self.items.values())
