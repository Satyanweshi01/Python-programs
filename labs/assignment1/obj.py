#Write program to implement id(), type(),sep,end, | , &, ^ , << ,>>.

a = 12
print(f"Object Id: {id(a)}")
print(f"Object Type: {type(a)}")

d = "11"
m = "08"
y = "2026"
print(d,m,y,sep="/",end="\n\n")

x = 8
y = 5
print(x|y)
print(x&y)
print(x^y)
print(x<<1)
print(x>>1)