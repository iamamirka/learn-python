emails = [
    "foo@ex.ex",
    "bar@ex.ex",
    "foobar@ex.ex"
    ]

index_0 = emails[0]
index_1 = emails[1]
index_2 = emails[2]

print(index_0, index_1, index_2)

# Augmented assigment
emails += ["123@ex.ex", "contact@ex.ex"]
print(emails)

# List concatenation
scores = [1, 2, 3] + [4, 5] + [6]
print("initial concatenated scores:", scores)

# modify a list in place
scores.append(7)
print("scores after appending 7:", scores)

scores.extend([8, 9])
print("scores after extending [8, 9]:", scores)

result = scores.pop(0)
print(result)

# insert into the list an index 3
scores.insert(3, "inserted!")
print("scores after inserting 'inserted!' at index 3:", scores)

# Remove element frpm list at index 3
scores.remove('inserted!')
print("scores after removing 'inserted!':", scores)

# Getting the size of lists
list_length = len([True, True, False])
print(list_length)

# Getting minimum and maximum values of list
my_list_numbers = [100, 200, 300]

list_max = max(my_list_numbers)
list_min = min(my_list_numbers)
print(list_max, list_min)

# Slicing lists
steps = [
    'wake up',
    'get out of bed',
    'make coffee',
    'go for walk',
    'start work'
]

print("steps are:", steps)
print("steps[0:2] are:", steps[0:2])
print("steps[0:] are:", steps[0:])
print("steps[:3] are:", steps[:3])

# Specify the stride as the third colon-separated element of a slice
print("steps[0:4:2] are:", steps[0:4:2])
print("steps[0::1] are:", steps[0::1])

# Negative numbers are valid
print('steps[-2] is', steps[-2])

# Syntax for reversing a list:
print("Reversing steps with steps [::-1] is:", steps[::-1])

# Reversing a string
print("This is an example"[::-1])

# Strings and Lists are both iterables
hello = "Hello"
some_list = ['h', 'e', 'l', 'l', 'o']

print(hello is hello[:]) # If we make slice operation with string, it points to the same object
print(some_list is some_list[:]) # If we make slice operation with list of strings, it always creates a new object

# Nesting Lists
matrix = [[0.3, 0.3, 0.2],
          [0.5, 0.1, 0.2],
          [0.3, 0.4, 0.2]]

jagged_list = [[1],
               [2, 3],
               [-2],
               [0, 3, 0, -1]]

nested = [1, [2, 3, [4, 5, 6]]]

print(matrix[0][1])
print(jagged_list[2][0])
print(nested[1][2][0])

for item in matrix:
    print(item)

# Tuples

# Tuples are immutable!
x = ('foo', 'bar', 'baz')
y = ['foo', 'bar', 'baz']
print(type(x), type(y))

y[0] = 'qwqw'
print(x[::-1])