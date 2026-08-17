#Write a Python program to find duplicate chacters in a string.
a = input("Enter the string: ")
storage = {}
for ch in a:
    if ch not in storage:
        storage[ch] = 1
    else:
        storage[ch] += 1
dup_list = []
for ch in storage:
    if storage[ch] > 1:
        dup_list.append(ch)
print(dup_list)
