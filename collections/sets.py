colors_1 = {"blue", "green", "red", "red"}
print(colors_1)

# Use set()
user_ids = set([123, 433, 222, 222, 222, 433])
print(user_ids)
user_ids_list = [123, 433, 222, 222, 222, 433]
print(set(user_ids_list))

s = {123, False, "foo"}
print(s)

# union
s1 = {1, 2, 3}
s2 = {4, 5, 6}
s3 = s1 | s2 # s3 = s1.union(s2)
print("Union of s1 | s2:", s3)

# intersections
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = s1 & s2 # s3 = s1.intersection(s2)
print("Intersection of s1 & s2:", s3)

# difference
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = s1 - s2 # s3 = s1.difference(s2)
print("Difference of s1 - s2:", s3)

s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = s2 - s1 # s3 = s2.difference(s1)
print("Difference of s2 - s1:", s3)

# Symmetric difference
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = s1 ^ s2 # s3 = s1.symmetric_difference(s2)
print("Symmetric difference of s1 ^ s2:", s3)

drinks = {"water", "tea", "coffee"}
drinks.add("mineral water")
drinks.remove("water")
# drinks.remove("wine") # throws error if "wine" not in set
drinks.discard("wine") # does nothing if "wine" not set
print(drinks)