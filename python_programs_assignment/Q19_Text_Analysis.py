# Q19 - Text Analysis (Alternative Version)

text = input("Enter text: ")

words = text.split()
vowels = "aeiou"

vowel_count = 0
consonant_count = 0

for char in text.lower():
    if char in vowels:
        vowel_count += 1
    elif char.isalpha():
        consonant_count += 1

print("Total words:", len(words))
print("Vowels:", vowel_count)
print("Consonants:", consonant_count)
print("Reversed:", text[::-1])