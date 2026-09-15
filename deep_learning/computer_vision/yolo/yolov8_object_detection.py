# Install required packages
# pip install ultralytics opencv-python matplotlib -q

from ultralytics import YOLO
import cv2
import matplotlib.pyplot as plt

# from google.colab import files

# Upload an image
# uploaded = files.upload()

# Load pretrained YOLOv8 model (nano version)
model = YOLO("yolov8n.pt")

# Get uploaded image path
# image_path = list(uploaded.keys())[0]

# Provide local image path
image_path = r"IMG_1154.JPG"

# Run detection
results = model(image_path)

# Plot annotated detection result
annotated_img = results[0].plot()

plt.figure(figsize=(8, 6))
plt.imshow(cv2.cvtColor(annotated_img, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.title("YOLOv8 Detection Result")
plt.show()

# Print detected objects
print("\nDetected Objects:\n")
for box in results[0].boxes:
    cls_id = int(box.cls[0])
    conf = float(box.conf[0])
    label = model.names[cls_id]
    print(f"{label} -> {conf:.2f}")
