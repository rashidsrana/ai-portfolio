"""
Task 2: Compare Two Sentences
Objective
Create a Python program that compares two sentences and finds the common words between them.
Instructions
1.	Accept two sentences from the user. 
2.	Convert both sentences to lowercase. 
3.	Remove punctuation marks (.,!?;:). 
4.	Split both sentences into words. 
5.	Find the words that appear in both sentences. 
6.	Remove duplicate common words. 
7.	Display: 
o	The common words. 
o	The total number of common words. 
o	The words that are unique to the first sentence. 
o	The words that are unique to the second sentence.
"""

import string

# Input from user
sentence1 = input("Enter Sentence 1: ")
sentence2 = input("Enter Sentence 2: ")

# Convert to lowercase
sentence1 = sentence1.lower()
sentence2 = sentence2.lower()

# Remove punctuation
sentence1 = sentence1.translate(str.maketrans('', '', string.punctuation))
sentence2 = sentence2.translate(str.maketrans('', '', string.punctuation))

# Tokenize sentences
words1 = sentence1.split()
words2 = sentence2.split()

# Convert to sets
set1 = set(words1)
set2 = set(words2)

# Find common and unique words
common_words = set1.intersection(set2)
unique_to_first = set1.difference(set2)
unique_to_second = set2.difference(set1)

# Display results
print("\nCommon Words :")
if common_words:
    for word in sorted(common_words):
        print(word)
else:
    print("None")

print("\nTotal Common Words:", len(common_words))

print("\nWords only in Sentence 1:")
if unique_to_first:
    for word in sorted(unique_to_first):
        print(word)
else:
    print("None")

print("\nWords only in Sentence 2:")
if unique_to_second:
    for word in sorted(unique_to_second):
        print(word)
else:
    print("None")