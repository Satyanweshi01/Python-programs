#Write a Python program to check whether a string is a palindrome
a = input("Enter the string: ").upper()
if a == a[::-1]:
    print("It is palindrome")
else:
    print("It is not palindrome")