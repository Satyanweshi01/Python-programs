a = [1,2,3]
b = [5,8,9]

c = zip(a,b) # returns zip object(iterator of tuples)
d = zip(a,b)
for i in c:
    print(i)
print(c)
print(list(d))