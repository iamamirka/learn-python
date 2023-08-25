numbers = [1, 34, 54, 24]
total_sum = 0

for n in numbers:
    total_sum += n
    print(total_sum)

# Loopnig over a dictionary

user = {
    "name"  : "foo",
    "age"   : 64,
    "email" : "foo@ex.ex"
}

for key in user:
    print(f"{key}\t => \t {user[key]}")