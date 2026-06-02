h = int(input("Enter the height: "))

for i in range(1,h+1):
    for j in range(h):
        print("*",end="")
    print("")
    h-=1