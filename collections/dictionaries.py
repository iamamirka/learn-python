# building a dictionary

customer_address = {
    "id"        : 23,
    "street"    : "123 Main St",
    "city"      : "Madison",
    "state"     : "WI",
    "zip"       : "53713",
    "is_active" : True
}

# accessing a value by key
city = customer_address["city"]
is_active = customer_address["is_active"]
print(f"City: {city}, Active? {is_active}")

# adding a key-value pair to dictionary
customer_address["phone"] = "555-555-1234"
print(customer_address["phone"])

# Nested dictionary
customer = {
    "name" : "Jane Doe",
    "age"  : 60,
    "is_employee" : True,
    "address" : customer_address
}

print(customer["address"]["state"])