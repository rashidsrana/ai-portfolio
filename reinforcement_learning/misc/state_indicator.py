import random

states = ["A", "B"]

transition = {"A": {"A": 0.7, "B": 0.3}, "B": {"A": 0.4, "B": 0.6}}

current_state = "A"
steps = 5

print("Start:", current_state)

for i in range(steps):

    rand = random.random()

    if current_state == "A":
        if rand < 0.7:
            current_state = "A"
        else:
            current_state = "B"
    else:
        if rand < 0.4:
            current_state = "A"
        else:
            current_state = "B"

    print(f"Step {i+1}: {current_state}")
