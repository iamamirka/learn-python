if 2 > 1:
    print("Ok!")

if 2 < 1:
    print("Ok!")
else:
    print("Bar!")

if 2 < 1:
    print("Foo")
elif 2 != 2:
    print("Bar")
else:
    print("Baz")


if 1 < 2 and "a" == "a":
    print("All good")

# An empty list is "Falsy"
errors = []

if not errors:
    print("No errors!")

if not 0:
    print("Zero 0 is Falsy")

if not "":
    print("Falsy")

if not set():
    print("Falsy")

if not range(0):
    print("Falsy")