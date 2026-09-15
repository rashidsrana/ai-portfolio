import random

states = ["Healthy", "Sick"]
observations = ["NormalTemp", "Fever"]

transition = {
    "Healthy": (["Healthy", "Sick"], [0.7, 0.3]),
    "Sick": (["Healthy", "Sick"], [0.4, 0.6]),
}

emission = {
    "Healthy": (["NormalTemp", "Fever"], [0.9, 0.1]),
    "Sick": (["NormalTemp", "Fever"], [0.2, 0.8]),
}

state = "Healthy"
print("\nHMM Simulation:")

for t in range(10):
    obs = random.choices(emission[state][0], emission[state][1])[0]

print(f"Time {t}: State={state}, Observation={obs}")

state = random.choices(transition[state][0], transition[state][1])[0]
