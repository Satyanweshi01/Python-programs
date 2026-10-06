a = [1,3,5]
b = map(lambda x:x+5,a) # returns map object(lazy iterator)
for i in b:
    print(i)
print(b)