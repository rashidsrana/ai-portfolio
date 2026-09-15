import random

states = ["Sunny", "Rainy"]

transition = {
    "Sunny": (["Sunny", "Rainy"], [0.8, 0.2]),
    "Rainy": (["Sunny", "Rainy"], [0.4, 0.6])
}

state = "Sunny"

print("Weather Simulation (Markov Chain):")
for day in range(10):
    print(f"Day {day}: {state}")
    next_states, probs = transition[state]
    state = random.choices(next_states, probs)[0]
