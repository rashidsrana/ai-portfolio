# Object Detection and Annotation Verification using Faster R-CNN

import torch
import torchvision
from torchvision import transforms
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Load pre-trained Faster R-CNN model
model = torchvision.models.detection.fasterrcnn_resnet50_fpn(weights="DEFAULT")
model.eval()

# COCO class labels
COCO_CLASSES = [
    "_background_",
    "person",
    "bicycle",
    "car",
    "motorcycle",
    "airplane",
    "bus",
    "train",
    "truck",
    "boat",
    "traffic light",
    "fire hydrant",
    "N/A",
    "stop sign",
    "parking meter",
    "bench",
    "bird",
    "cat",
    "dog",
]

# Load image
# image_path = "/content/trucks-vs-cars.webp"
image_path = r"IMG_1154.JPG"
image = Image.open(image_path).convert("RGB")

# Transform image
transform = transforms.ToTensor()
image_tensor = transform(image)

# Run object detection
with torch.no_grad():
    predictions = model([image_tensor])

# Extract predictions
boxes = predictions[0]["boxes"]
labels = predictions[0]["labels"]
scores = predictions[0]["scores"]

# Confidence threshold
threshold = 0.5

# Store detected labels
detected_objects = []

# Display image
fig, ax = plt.subplots(1, figsize=(12, 8))
ax.imshow(image)

for box, label, score in zip(boxes, labels, scores):
    if score > threshold:

        x1, y1, x2, y2 = box.numpy()

        class_name = COCO_CLASSES[label] if label < len(COCO_CLASSES) else "Unknown"
        detected_objects.append(class_name)

        rect = patches.Rectangle(
            (x1, y1), x2 - x1, y2 - y1, linewidth=2, edgecolor="red", facecolor="none"
        )
        ax.add_patch(rect)

        ax.text(
            x1, y1, f"{class_name}: {score:.2f}", color="white", backgroundcolor="red"
        )

plt.title("Object Detection Results")
plt.axis("off")
plt.show()

# ---------------------------------------------------------
# Annotation Verification
# ---------------------------------------------------------

existing_annotations = ["car", "person", "dog"]

detected_set = set(detected_objects)
annotated_set = set(existing_annotations)

print("\n===== Annotation Verification Report =====")

# Correct annotations
correct = annotated_set.intersection(detected_set)

# Missing labels
missing_labels = detected_set - annotated_set

# Incorrect annotations
incorrect_labels = annotated_set - detected_set

print("Correct Annotations:")
for item in correct:
    print("-", item)

print("\nMissing Labels (Detected but Not Annotated):")
for item in missing_labels:
    print("-", item)

print("\nAnnotations Requiring Review:")
for item in incorrect_labels:
    print("-", item)

print("\nSummary")
print("Correct:", len(correct))
print("Missing Labels:", len(missing_labels))
print("Need Review:", len(incorrect_labels))
