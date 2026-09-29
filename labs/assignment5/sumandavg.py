#4. Find the Sum and Average: Write a Python program to calculate the sum and average of values stored in a dictionary containing marks of five subjects
d = eval(input("Enter dict: "))
s = sum(list(d.values()))
avg = s/len(d)
print("Sum: ",s ,"\nAverage: ", avg)