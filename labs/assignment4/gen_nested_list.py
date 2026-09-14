#10.Generating a nested list by taking user input.
m = int(input("Enter rows: "))
n = int(input("Enter columns: "))
s = []
for i in range(m):
    k = []
    for j in range(n):
        l = input("Enter data: ")
        k.append(l)
    s.append(k)
print(s)