#6.Concatenate two tuples into one.

a = tuple(input("Enter tuple1: "))
print(a)
b = tuple(input("Enter tuple2: "))
print(b)
c = tuple(list(a)+list(b))
print("Joined tuple:",c)