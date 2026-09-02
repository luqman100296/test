import re

text1 = """Python is a powerful programming language that is widely used for web development, data analysis, artificial intelligence, and more. 
It is known for its simplicity and readability, making it a great choice for beginners and experienced developers alike. 
Python's extensive libraries and frameworks allow developers to build complex applications quickly and efficiently. 
Whether you're interested in building websites, analyzing data, or creating machine learning models, Python provides the tools and resources you need to succeed in the world of programming."""

print(len(text1))
char_count = len(text1)
word_count = len(text1.split())
sentence_count = len(re.split(r'[.!?]+', text1.strip('.!? ')))

print("Character count:", char_count)
print("Word count:", word_count)
print("Sentence count:", sentence_count)

print(text1[0])
print(text1[-1])
print(text1[0:20])
print(text1[:30])
print(text1[555:])

word = "wood"

tongue_twister_1 = f"How much {word} would a {word}chuck chuck if a {word}chuck could chuck {word}?"
tongue_twister_2 = "How much {} would a {}chuck chuck if a {}chuck could chuck {}?". format(word, word, word, word)

print(tongue_twister_1)
print(tongue_twister_2)

print(word.upper())
print(word.lower())
print(word.title())
print(word.replace("wood", "Jane"))