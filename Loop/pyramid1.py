
h = int(input("Enter the height: "))

# for i in range(1,h+1):
#     print("*"*i)

for i in range(1,h+1):
    for j in range(i):
        print("*",end="")
    print("")
    