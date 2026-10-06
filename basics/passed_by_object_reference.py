# in python variables are passed by object reference
def func(x):
    x.append(5) # here x = a so we are mutating the a's list via x 
    x = [10,20] # but here another list's reference is getting assigned to the x
    print(f"x = {x}") # x's new value is getting printed

a = [1,3,4]

print(f"old value of a = {a}")# func(a) -> does not reassign value of a or changes it
func(a)# here object reference of the [1,3,4] is passing to x via a
print(f"new value of a = {a}")# func(a) -> does not reassign value of a or changes it

