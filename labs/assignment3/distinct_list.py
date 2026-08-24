#3.Remove duplicates from a list.
data = input("Enter integer with space in between: ").split()
data = list(set(data))
print(data)