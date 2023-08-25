# In Python there are 3 types of numbers
# - int (integers)
# - float (floating point numbers)
# - complex (complex numbers)

x = 24            # int - no maximum size!
y = 32.10         # float (beware of dloating point error!)
z = complex(2, 4) # complex

# Boolean types in Pytho are subclass of numbers!
print(True == 1)            # => True
print(False == 0)           # => True
print(True + True + True)   # => 3
print(True / True)          # => 1.0
print(True / False)         # => ZeroDivisionError: division by zero
