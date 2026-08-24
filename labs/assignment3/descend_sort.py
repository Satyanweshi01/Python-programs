#7.Take a list and sort that in descending order.
data = input("Enter integer with space in between: ").split()
new_data = list(map(int, data))
new_data.sort(reverse=True)
print(new_data)