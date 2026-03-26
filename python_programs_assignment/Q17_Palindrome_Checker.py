# Q17 - Palindrome Check (Alternative Version)

word = input("Enter text: ")
cleaned_word = word.lower()

if cleaned_word == cleaned_word[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")