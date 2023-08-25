# A simple function
def print_name():
    my_name = "Amir"
    print(my_name)

print_name()


# A function with single parameter
def calculate_days_old(age_in_years):
    days_in_year = 365
    age_in_days = age_in_years * days_in_year
    report = f"I'm about {age_in_days} days old"
    print(report)

# calculate_days_old("Hello") => I'm about {Hello 365 раз} days old, ошибок нет
calculate_days_old(25)

# A dunc that takes single parameter
# And returns a value
def get_days_old(age_in_years):
    days_in_year = 365
    return age_in_years * days_in_year

days_old = get_days_old(25)
print(days_old)