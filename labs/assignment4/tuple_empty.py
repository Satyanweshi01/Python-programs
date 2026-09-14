#2.Write a python program to check if a tuple is empty.

a = tuple(input("Enter tuple:"))
print(a)
if len(a) == 0:
    print("Tuple is empty")
else:
    print("Tuple is not empty")