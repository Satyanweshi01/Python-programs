a = [13,5,8,12,11,18]

b = filter(lambda x: x > 10,a) #returns filter object(lazy iterator)


print(list(b))
for i in b:
    print(i)