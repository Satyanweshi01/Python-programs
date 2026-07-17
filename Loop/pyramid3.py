
h = int(input("Enter the height: "))

for i in range(1,h+1):
    for k in range(h-i):
        print(" ",end="")
    for j in range(i*2-1):
        print("*",end="")
    print("")
