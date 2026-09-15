"""

Task
Think of your robot’s wheel like a circle with 360 degrees.
You’ve attached an encoder that gives 360 pulses for one full turn — that’s 1 pulse per degree.
As the motor spins, your code counts the pulses.

But instead of tracking thousands of pulses forever, you want to know where the wheel is right now in the current turn — just like reading a compass or clock: always between 0 and 359

"""


# ============================================
# Wheel Position from Encoder Pulses
# ============================================

PULSES_PER_REV = 360   # 360 pulses = 360 degrees

def get_wheel_position(pulse_count):
    """
    Convert total pulses into current wheel position (0–359 degrees).
    """
    return pulse_count % PULSES_PER_REV


# ============================
# Example Usage
# ============================

pulses = 9872   # total pulses counted so far
position = get_wheel_position(pulses)

print("Total pulses:", pulses)
print("Wheel position (degrees):", position)
