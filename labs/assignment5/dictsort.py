#8. Sort a Dictionary: Write a Python program to sort a dictionary by its keys in ascending order.
d = eval(input("Enter dict: "))

print(d.items())
print(list(d.items()).sort())
print(dict(d.items()))