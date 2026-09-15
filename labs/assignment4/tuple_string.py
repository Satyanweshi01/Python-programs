#4.Convert a tuple to a single string.
a = tuple(input("Enter tuple:"))
print(a)
b= list(a)
c = "".join(b)
print(c)
print(type(c))