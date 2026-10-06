e = enumerate(["a", "b", "c"]) # returns enumerate object(iterator of tuples)

print(next(e))
print(next(e))
print(next(e))

a = [1,3,5]
for i,v in enumerate(a):
    print(i,v)