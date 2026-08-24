#5.Merge two lists into one.
data1 = input("Enter integer with space in between for list1: ").split()
data2 = input("Enter integer with space in between for list2: ").split()

data1.extend(data2)

print(data1)
