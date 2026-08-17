#Write a Python program to reverse each word of a sentence without changing the position of the words

a = input("Enter the string: ")
wordlist = a.split()
new_wordlist = []
#print(wordlist)
for word in wordlist:
    new_wordlist.append(word[::-1])

b = " ".join(new_wordlist)
print(b)