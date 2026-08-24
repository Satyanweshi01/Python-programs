#1.Write a python program to find the sum of all elements of a list.
data = input("Enter integer with space in between: ").split()

new_data = map(int, data)

print(f"The sum: {sum(new_data)}")
