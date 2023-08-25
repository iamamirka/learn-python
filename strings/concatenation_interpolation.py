# Usinag a variable
first_name = "Amir"

#String concatenation
print("My name is " + first_name + "!")

#String interpolation - f-strings
print(f"My name is {first_name} {first_name}!")

#String interpolation - %-formatting
print("My name is %s!" % first_name)

#String interpolation - %-formatting multiple
last_name = "Ibatullin"
print("My name is %s %s!" % (first_name, last_name))

#String interpolation = str.format()
print("My name is {}!".format(first_name))