"""
Builds a Customer report for 
Sales Orders
"""

def print_customer_address(name, city, state, street):
    """ Prints a composed address """
    customer_address = f"{name}\n{street}\n{city}, {state}"
    print(customer_address)

def calculate_order_total(qty, cost):
    """ Multiplies qty by cost to calculate total """
    return qty * cost

def print_customer_report():
    """ Prints a customer report """
    print("Shipping address:")
    print_customer_address(
        "Some Name",
        "San Diego",
        "CA",
        "123 Main St.")
    print("Order total:")
    order_total = calculate_order_total(10, 2.99)
    rounded = round(order_total, 3)
    print(rounded)

print_customer_report()