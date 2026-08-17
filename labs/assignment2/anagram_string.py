# Write a Python program to check whether two strings are anagrams

def count(string, dictionary):
    for ch in string:
        if ch not in dictionary:
            dictionary[ch] = 1
        else:
            dictionary[ch] += 1


a = input("Enter the string1: ")
b = input("Enter the string2: ")

d1 = {}
count(a,d1)
d2 = {}
count(b,d2)

if d1 == d2:
    print("These are anagrams")
else:
    print("These are not anagrams")