

import random

# Training data
data = [
    ("hello", "greeting"),
    ("hi there", "greeting"),
    ("good morning", "greeting"),
    ("how are you", "not_greeting"),
    ("I like pizza", "not_greeting"),
    ("today is sunny", "not_greeting")
]

actions = ["greeting", "not_greeting"]

# Q-table
Q = {}

# Training
for episode in range(1000):
    sentence, correct_action = random.choice(data)
    words = sentence.lower().split()
    for word in words:
        if word not in Q:
            Q[word] = {"greeting": 0, "not_greeting": 0}

    action = random.choice(actions)
    reward = 1 if action == correct_action else -1
    Q[word][action] += 0.1 * reward

# Testing
user_text = input("Enter a sentence: ")

greeting_score = 0
not_greeting_score = 0

for word in user_text.lower().split():
    if word in Q:
        greeting_score += Q[word]["greeting"]
        not_greeting_score += Q[word]["not_greeting"]

if greeting_score > not_greeting_score:
    print("Prediction: Greeting")
else:
    print("Prediction: Not Greeting")