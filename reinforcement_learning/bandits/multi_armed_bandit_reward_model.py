import random

trials = 50
reward_A = 0
reward_B = 0

for _ in range(trials):

    choice = random.choice(["A", "B"])

    if choice == "A":
        reward_A += random.randint(0, 1)
    else:
        reward_B += 1

print("Total reward of A:", reward_A)
print("Total reward of B:", reward_B)

if reward_A > reward_B:
    print("Machine A performed better")
elif reward_B > reward_A:
    print("Machine B performed better")
else:
    print("Both machines performed equally")
