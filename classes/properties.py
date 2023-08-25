# In Python, there isn't a direct analog to C#'s properties, 
# but you can achieve similar functionality using properties and getters/setters. 
# In C#, properties are a way to encapsulate private fields and provide controlled access to them with custom logic. 
# In Python, you can use the @property decorator to achieve similar behavior.

class MyClass:
    def __init__(self):
        self._value = 0  # Conventionally, use a single underscore for "private" attributes

    @property
    def value(self):
        print("Getting value")
        return self._value

    @value.setter
    def value(self, new_value):
        print("Setting value")
        if new_value >= 0:
            self._value = new_value
        else:
            print("Value cannot be negative")

# Usage
obj = MyClass()
print(obj.value)  # Calls the getter method
obj.value = 5     # Calls the setter method
print(obj.value)
obj.value = -2    # Tries to set a negative value


# In this example, the @property decorator is used to create a getter method, 
# and the @value.setter decorator is used to create a setter method. 
# These methods allow you to encapsulate the underlying _value attribute with custom logic.

# Remember that in Python, there is no strict concept of private or protected members as in C#. 
# The single leading underscore (_value) is a convention indicating that the attribute is intended to be "protected" or internal, 
# but it can still be accessed directly if desired. 
# Double leading underscores (__value) are used for name mangling to make attributes harder to access, but they are still not truly private.

# Also, note that Python's philosophy is generally more lenient regarding encapsulation 
# and encourages developers to be responsible for their own access and usage of attributes.
