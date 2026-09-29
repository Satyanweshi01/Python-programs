#9. Character Frequency: Write a Python program to count the frequency of each character in a given string using a dictionary.
s = input("Enter string: ")
d = {}
for i in s:
    if i in d:
        d[i]+=1
    elif i == " ":
        continue
    else:
        d[i] = 1
print(d)