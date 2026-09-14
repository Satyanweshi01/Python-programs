#1.Convert a Tuple to a List, insert any element and then convert back.
a = tuple(input("Enter tuple: "))
print(a)
li = list(a)
b = input("Enter data: ")
li.append(b)
a = tuple(li)
print(a)