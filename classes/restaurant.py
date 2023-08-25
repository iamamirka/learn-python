import lunch_menu
# from lunch_menu import LunchMenu -> helps to avoid extra filename writing

cafe_menu = lunch_menu.LunchMenu()
cafe_menu.add_beverage('tea')
cafe_menu.add_beverage('coffee')
cafe_menu.add_food('bagel')
cafe_menu.generate()