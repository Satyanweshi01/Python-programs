#Write a Python program to find the frequency of each chacter in a string.

a = input("Enter the string: ")
storage = {}
for ch in a:
    if ch not in storage:
        storage[ch] = 1
    else:
        storage[ch] += 1
print(storage)
