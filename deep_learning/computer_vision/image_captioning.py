#  Upload an image and generate a caption using a pre‑trained BLIP model.”
"""
Task: Image Captioning Using BLIP
Objective:  
Generate a text description (caption) for an uploaded image.

Steps in the screenshot:

Upload image

Load BLIP model

Process image

Generate caption

Decode caption
===========================================
"""

from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
#from google.colab import files
import torch

"""
# Following code is for google colab. If you are using VS Code, you can set the image path manually.
# Upload image
uploaded = files.upload()

# Get uploaded file name
image_path = list(uploaded.keys())[0]

# Open image
image = Image.open(image_path).convert("RGB")
"""

# ---------------------------------------------------------
# 1. Set image path manually (VS Code)
# ---------------------------------------------------------
image_path = r"C:\Users\cyber\OneDrive\Pictures\IMG_1161.jpg"
image = Image.open(image_path).convert("RGB")

# Load BLIP model and processor
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Prepare image
inputs = processor(image, return_tensors="pt")

# Generate caption
output = model.generate(**inputs, max_length=30)

# Decode caption
caption = processor.decode(output[0], skip_special_tokens=True)

print("Generated Caption:", caption)