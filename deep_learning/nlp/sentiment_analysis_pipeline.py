"""
Extracted Text from Screenshot
Task 1: Count Positive and Negative Words  
Objective  
Create a Python program that determines whether a sentence is positive, negative, or neutral.

Instructions

Accept a sentence from the user.

Convert it to lowercase.

Remove punctuation (.,!;?).

Split the sentence into words.

Use these word lists:
• Positive: ["good", "great", "happy", "love", "excellent"]
• Negative: ["bad", "sad", "hate", "terrible", "poor"]

Count the positive and negative words in the sentence.

Display:
• Positive word count
• Negative word count
• Overall sentiment (Positive, Negative, or Neutral)
========================================================
"""

import string

# Positive and negative word lists
positive_words = ["good", "great", "happy", "love", "excellent"]
negative_words = ["bad", "sad", "hate", "terrible", "poor"]

# 1. Accept a sentence from the user
sentence = input("Enter a sentence: ")

# 2. Convert to lowercase
sentence = sentence.lower()

# 3. Remove punctuation
sentence = sentence.translate(str.maketrans("", "", string.punctuation))

# 4. Split into words
words = sentence.split()

# 5. Count positive and negative words
positive_count = sum(word in positive_words for word in words)
negative_count = sum(word in negative_words for word in words)

# 6. Determine overall sentiment
if positive_count > negative_count:
    sentiment = "Positive"
elif negative_count > positive_count:
    sentiment = "Negative"
else:
    sentiment = "Neutral"

# 7. Display results
print("Positive words:", positive_count)
print("Negative words:", negative_count)
print("Overall Sentiment:", sentiment)