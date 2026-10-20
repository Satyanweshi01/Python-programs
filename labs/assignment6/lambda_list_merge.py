a = [1,2,3]
b = [3,2,1]

c = list(map(lambda x : x[0]*x[1],zip(a,b))) # returns zip object(iterator of tuples)
print(c)