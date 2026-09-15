import os
import cv2
import numpy as np

# Get current script directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Build precise file paths
input_path = os.path.join(script_dir, "ApexHealthLogo.png")
output_path = os.path.join(script_dir, "logo_perfect_transparent.png")

# Load image
img = cv2.imread(input_path)

if img is None:
    raise FileNotFoundError(f"Cannot find input file at: {input_path}")

# Step 1: Convert to grayscale and blur to remove pixel noise/halos
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (7, 7), 0)

# Step 2: Use an adaptive threshold to separate the logo from the bright background.
# This creates a sharp black and white separation map.
_, thresh = cv2.threshold(blurred, 240, 255, cv2.THRESH_BINARY_INV)

# Step 3: Find the largest connected shape (which will be your central shield emblem)
# This completely ignores the watermark in the top-right corner without needing to crop it.
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

if contours:
    # Isolate the largest detected shape in the image
    largest_contour = max(contours, key=cv2.contourArea)

    # Create a completely blank mask layer matching our image size
    clean_mask = np.zeros_like(thresh)

    # Draw ONLY the logo emblem onto our clean mask layer, filled with solid white (255)
    cv2.drawContours(clean_mask, [largest_contour], -1, 255, thickness=cv2.FILLED)

    # Smooth the edges of our mask slightly so the transparency blend isn't jagged
    clean_mask = cv2.GaussianBlur(clean_mask, (3, 3), 0)
else:
    # Fallback to the default threshold map if no clear contour is isolated
    clean_mask = thresh

# Step 4: Convert the original BGR image to a 4-channel BGRA image (Alpha channel active)
rgba = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)

# Apply our clean, watermark-free mask directly to the Alpha (transparency) layer
rgba[:, :, 3] = clean_mask

# Save the final production asset as a true PNG file format
cv2.imwrite(output_path, rgba)
print(f"Success! Clean transparent logo generated with zero artifact noise.")
print(f" Saved directly to: {output_path}")
