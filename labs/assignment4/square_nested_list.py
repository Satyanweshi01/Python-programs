#9.Square the each element of a nested list.
m = int(input("Enter rows: "))
n = int(input("Enter columns: "))
s = []
for i in range(m):
    k = []
    for j in range(n):
        l = int(input("Enter data: "))
        k.append(l)
    s.append(k)

for i in range(m):
    for j in range(n):
        s[i][j]=s[i][j]*s[i][j]
        
print(s)
