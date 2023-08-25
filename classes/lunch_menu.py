class LunchMenu:
    """Tracks items on the lunch menu"""
    def __init__(self):
        self.beverages = []
        self.food = []
    
    def add_food(self, food):
        """Adds food to menu"""
        self.food.append(food)
    
    def add_beverage(self, beverage):
        """Adds food to menu"""
        self.beverages.append(beverage)

    def generate(self):
        print("Food:")
        for food in self.food:
            print('- ' + food)

        print("Beverages:")
        for beverage in self.beverages:
            print('- ' + beverage)

if __name__ == "__main__":
    # create an instance of LunchMenu
    my_menu = LunchMenu()

    # add food and beverages to the instance
    my_menu.add_food('soup')
    my_menu.add_food('sandwich')
    my_menu.add_food('salad')
    my_menu.add_beverage('coffee')
    my_menu.add_beverage('wine')

    # print the menu on the instance
    my_menu.generate()


    # --------
    veg_menu = LunchMenu()
    veg_menu.add_food('cabbage soup')
    veg_menu.add_food('black bean soup')
    veg_menu.add_food('corn chowder')

    meat_menu = LunchMenu()
    meat_menu.add_food('chicken sandwich')
    meat_menu.add_food('beef soup')

    print('Vegetarian menu:')
    veg_menu.generate()
    print('Non-vegetarian menu:')
    meat_menu.generate()