#!/usr/bin/env python3.7

message = input("Enter a message: ")

print("Lowercase:", message.lower())
print("Uppercase:", message.upper())
print("Capitalize:", message.capitalize())
print("Title Case:", message.title())

words = message.split()
print("words:", words)

sorted_words = sorted(words)
print("Sorted:", sorted_words)
print("First word:", sorted_words[0])
print("Last word:", sorted_words[-1])