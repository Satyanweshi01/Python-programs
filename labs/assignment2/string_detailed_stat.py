#Write a Python program to count uppercase letters, lowercase letters, digits, and special characters in a string.

a = input("Enter the string: ")
up_letter = 0
sm_letter = 0
digits = 0
sp_char = 0

for ch in a:

    if ch.isupper():
        up_letter += 1
    elif ch.islower():
        sm_letter += 1
    elif ch.isdigit():
        digits += 1
    elif not ch.isspace():
        sp_char += 1

print(f"Upper case: {up_letter}")
print(f"Small case: {sm_letter}")
print(f"Digits: {digits}")
print(f"Special characters: {sp_char}")