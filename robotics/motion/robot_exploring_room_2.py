"""
Task
A small robot is exploring a room. The room has some open paths and some obstacles like boxes or walls. The robot wants to move from one place to another without bumping into anything.

To do this, the robot follows some basic rules. First, it checks if the path in front is clear. If it is, the robot moves forward. If the front is blocked, it looks to the right. If the right side is clear, the robot turns and moves that way. If both front and right are blocked, the robot stops and waits.

This way, the robot makes smart decisions step by step, just by checking its surroundings. The rules can be written in a simple table or using easy logic in a program.

Front	Right	Action
True	True	Move Forward
True	False	Move Forward
False	True	Turn Right
False	False	Stop


"""


# ============================================
# Robot Movement Logic Based on Sensor Inputs
# ============================================

def robot_action(front_clear, right_clear):
    """
    Decide robot movement based on front and right sensor readings.
    front_clear: True/False
    right_clear: True/False
    """

    if front_clear and right_clear:
        return "Move Forward"
    elif front_clear and not right_clear:
        return "Move Forward"
    elif not front_clear and right_clear:
        return "Turn Right"
    else:
        return "Stop"


# ============================
# Test the logic
# ============================

tests = [
    (True, True),
    (True, False),
    (False, True),
    (False, False)
]

for front, right in tests:
    print(f"Front={front}, Right={right} -> Action: {robot_action(front, right)}")
