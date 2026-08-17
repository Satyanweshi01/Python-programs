#Write a Python program to convert uppercase letters into lowercase without using the lower() function

a = input("Enter the string: ")
b=""
for ch in a:
    if ch.isalpha():
        new_char = chr(ord(ch)+32) 
        b+=new_char
    else:
        b+=ch
print(b)
