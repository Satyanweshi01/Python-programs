#8.Take a input of a list of integers and print them all using slicing.
data = input("Enter integer with space in between: ").split()
new_data = list(map(int, data))

print(new_data[:])

