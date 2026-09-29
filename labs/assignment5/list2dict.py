#7. Create a Dictionary from Two Lists: Write a Python program to create a dictionary using two lists, where one list contains keys and the other contains values
l1 = eval(input("Enter key list: "))
l2 = eval(input("Enter value list: "))
d = {}
for i in range(len(l1)):
    d[l1[i]] = l2[i]
print(d)