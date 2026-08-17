#Write a Python program to check whether a string starts and ends with the same character.

a = input("Enter the string: ").upper()
if a[0] == a[-1]:
    print("This string starts and ends with same character")
else:
    print("This string does not starts and ends with same character")

