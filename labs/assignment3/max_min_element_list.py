#4.Find the maximum and minimum element from a list.
data = input("Enter integer with space in between: ").split()
new_data = list(map(int, data))

print(f"The Maximum element: {max(new_data)}")
print(f"The Maximum element: {min(new_data)}")