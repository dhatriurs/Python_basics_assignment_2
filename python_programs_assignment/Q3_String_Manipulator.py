# Q3 - String Analysis Program
# This version stores results in variables before printing.

user_input = input("Enter a sentence: ")

length_with_space = len(user_input)
length_without_space = len(user_input.replace(" ", ""))
word_list = user_input.split()

print("\nSentence Analysis")
print("-----------------")
print("Original text:", user_input)
print("Characters (with spaces):", length_with_space)
print("Characters (without spaces):", length_without_space)
print("Number of words:", len(word_list))
print("Uppercase:", user_input.upper())
print("Lowercase:", user_input.lower())
print("Title Case:", user_input.title())

if len(word_list) > 0:
    print("First word:", word_list[0])
    print("Last word:", word_list[-1])

print("Reversed text:", user_input[::-1])