import unittest
from shopping_cart import ShoppingCart

class TestShoppingCart(unittest.TestCase):

    INVENTORY = {
        'apple' : 0.40,
        'orange': 0.80,
        'potato': 0.20
    }

    sut = ShoppingCart(INVENTORY)

    def test_add_item_given_new_item_adds_new_item_to_cart(self):
        self.sut.add_item('apple', 8)
        self.assertEqual(self.sut.items_in_cart, {'apple': 8})

    def test_add_item_given_multiple_new_item_adds_new_item_to_cart(self):
        sut = ShoppingCart(self.INVENTORY)
        sut.add_item('apple', 8)
        sut.add_item('orange', 1)
        self.assertEqual(sut.items_in_cart, {'apple': 8, 'orange': 1})

    def test_add_item_given_item_not_in_database_does_not_update_cart(self):
        self.sut.add_item('potato', 8)
        self.sut.add_item('car', 2)
        self.sut.add_item('house',10)
        self.assertEqual(self.sut.items_in_cart, {'potato': 8})

    def test_add_item_given_existing_item_increases_qty(self):
        self.sut.add_item('apple', 10)
        self.sut.add_item('apple', 20)
        self.sut.add_item('apple', 30)
        self.assertEqual(self.sut.items_in_cart, {'apple': 60})

    def test_add_item_given_negative_item_does_not_upgrade_cart(self):
        self.sut.add_item('apple', 10)
        self.sut.add_item('apple', -20)
        self.sut.add_item('apple', 30)
        self.assertEqual(self.sut.items_in_cart, {'apple': 40})

    def test_calculate_total_given_added_item_sets_total_cost(self):
        self.sut.add_item('apple', 8)
        self.sut.add_item('orange', 1)
        total = self.sut.calculate_total()
        self.assertEqual(total, 4.0)

if __name__ == '__main__':
    unittest.main()