from controller import Robot, Camera, Motion

TIME_STEP = 32

robot = Robot()

# --- Devices ---
camera = robot.getDevice("CameraTop")
camera.enable(TIME_STEP)

# Walking motion (use built-in NAO walk or your own)
walk_motion = Motion("Nao_Walk.motion")  # ensure this exists in your project

# Arm joints (left arm)
ARM_JOINTS = [
    "LShoulderPitch",
    "LShoulderRoll",
    "LElbowYaw",
    "LElbowRoll",
    "LWristYaw",
    "LHand",
]

joints = {name: robot.getDevice(name) for name in ARM_JOINTS}
for j in joints.values():
    j.setPosition(float("inf"))
    j.setVelocity(1.0)


# --- Helper functions ---


def walk_forward(steps=10):
    """Walk NAO forward using motion file."""
    for _ in range(steps):
        walk_motion.play()
        robot.step(TIME_STEP)


def move_arm_to_object():
    """Move arm to approximate object position in front of robot."""
    joints["LShoulderPitch"].setPosition(0.4)
    joints["LShoulderRoll"].setPosition(0.2)
    joints["LElbowYaw"].setPosition(-1.0)
    joints["LElbowRoll"].setPosition(-0.5)
    joints["LWristYaw"].setPosition(0.0)


def grasp_object():
    """Close hand to grasp object."""
    joints["LHand"].setPosition(0.0)  # closed


def lift_object_to_face():
    """Lift object to face level for inspection."""
    joints["LShoulderPitch"].setPosition(-0.2)
    joints["LShoulderRoll"].setPosition(0.1)
    joints["LElbowRoll"].setPosition(-1.0)


def detect_object_simple():
    """
    Simple placeholder detection:
    In a real solution, you’d process camera image.
    Here we assume object is in front.
    """
    return True


# --- Main loop ---

state = "SEARCH"

while robot.step(TIME_STEP) != -1:
    if state == "SEARCH":
        # Use camera to detect object (simplified)
        if detect_object_simple():
            state = "APPROACH"

    elif state == "APPROACH":
        # Walk towards object
        walk_forward(steps=12)
        state = "GRASP"

    elif state == "GRASP":
        move_arm_to_object()
        # let arm settle
        for _ in range(10):
            robot.step(TIME_STEP)
        grasp_object()
        for _ in range(10):
            robot.step(TIME_STEP)
        state = "INSPECT"

    elif state == "INSPECT":
        lift_object_to_face()
        for _ in range(10):
            robot.step(TIME_STEP)

        # Capture image from camera
        image = camera.getImage()
        # You can save or process image here if needed
        print("Object inspected using NAO camera.")
        break
