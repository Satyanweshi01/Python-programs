#1. Define a function to find out maximum and minimum element in a tuple.
user_input = eval(input("Enter tuple: "))

def max_min(inputs):
    print("Max: ",max(inputs),"Min: ",min(inputs))
max_min(user_input) 