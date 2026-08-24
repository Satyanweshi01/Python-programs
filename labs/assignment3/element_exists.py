#10.Check if the particular element exists in list or not.
data1 = input("Enter data: ").split()
key = input("Element to find: ")
if key in data1:
    print("The element is present in the list")
else:
    print("The element is not present in the list")