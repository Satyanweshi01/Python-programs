#Write a Python program to count the number of vowels and consonants in a string.
a = input("Enter the string: ").upper()
no_of_vowels = 0
no_of_consonants = 0
for ch in a:
    if ch.isalpha():
        if ch in "AEIOU":
            no_of_vowels = no_of_vowels + 1
        else: 
            no_of_consonants = no_of_consonants + 1

print(f"No of vowels: {no_of_vowels}")
print(f"No of consonants: {no_of_consonants}")