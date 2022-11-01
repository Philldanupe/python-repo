#!/usr/bin/env python3.7

# Python impementation here

message = input("Enter a message: ")

print("Lowercase:", message.lower())
print("Uppercase:", message.upper())
print("Capitalized:", message.capitalize())
print("Title Case:", message.title())

# create a list that splits the words

words = message.split()
print("Words:", words)

# sort words in string alphabetically and print first and last word

sorted_words = sorted(words)
print("Alphabetic First Word:", sorted_words[0])
print("Alphabetic Last Word:", sorted_words[-1])


