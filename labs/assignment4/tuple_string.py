#4.Convert a tuple to a single string.
a = tuple(input("Enter tuple:"))
print(a)
b= ""
for i in a:
    b+=i
print(b)