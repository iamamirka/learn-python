class ShoppingCart:
    """
    Tracks items in customer shopping cart
    and calculates grand total
    """

    def __init__(self, database):
        self.items_in_cart = {}
        self.database = database

    def add_item(self, item, qty):
        """
        Accepts an item tuple (name, price) and qty and updates items_in_cart
        :param item: string name of item to add
        :param qty: quantity of items to add
        :return: None
        """
        try:
            if item not in self.database.keys():
                print(f'No item with name {item} in inventory database.')
                return
            
            if not qty > 0:
                print('Cannot add negative item quantity to cart')
                return
            
            if item not in self.items_in_cart.keys():
                self.items_in_cart[item] = qty

            else:
                self.items_in_cart[item] += qty

        except AttributeError as e:
            print('There was an error while adding item(s) to cart.')
            print(e)

        except Exception as e:
            print('There was an error while adding item(s) to cart.')
            print(e)

    def calculate_total(self):
        """
        Calculates the total price of items added to cart
        :return: Grand total of all items in cart
        """
        total_cost = 0.0
        for item, qty in self.items_in_cart.items():
            unit_price = self.database[item]
            total_cost += unit_price * qty
        return total_cost