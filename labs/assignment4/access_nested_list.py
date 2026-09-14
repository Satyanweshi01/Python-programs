#8.Access the elements of s nested list by taking user input.

m = int(input("Enter rows: "))
n = int(input("Enter columns: "))
s = []
for i in range(m):
    k = []
    for j in range(n):
        l = input("Enter data: ")
        k.append(l)
    s.append(k)

r = int(input("Enter row no: ")) 
c = int(input("Enter column no: "))

element = s[r-1][c-1]
print("The Element: ",element)