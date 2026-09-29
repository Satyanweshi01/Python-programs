#2. Check Whether a Key Exists: Write a Python program to check whether a particular key exists in a dictionary
def keysearch(d,key):
    for i in d.keys():
        if key == i:
            return "Key is found"
    return "Key not found"

d = eval(input("Enter dict: "))
key = input("Enter the key you want to start: ")

print(keysearch(d,key))