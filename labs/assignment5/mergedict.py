#6. Merge Two Dictionaries: Write a Python program to merge two dictionaries into a single dictionary.
d1 = eval(input("Enter dict: "))
d2 = eval(input("Enter dict: "))
d1.update(d2)
print(d1)
merged = d1|d2
merged1 = {**d1,**d2}
print(merged)
print(merged1)