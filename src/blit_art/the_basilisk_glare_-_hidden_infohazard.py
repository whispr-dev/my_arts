import numpy as np
import cv2
import matplotlib.pyplot as plt

# Function to generate a hidden "face" in the pattern
def generate_hidden_basilisk(size=512):
    img = np.zeros((size, size, 3), dtype=np.uint8)

    # Generate an eerie, ghostly face using simple shapes
    center = (size // 2, size // 2)
    
    # Eyes (glowing, hidden effect)
    cv2.circle(img, (center[0] - 80, center[1] - 50), 40, (255, 255, 255), -1) # Left eye
    cv2.circle(img, (center[0] + 80, center[1] - 50), 40, (255, 255, 255), -1) # Right eye
    
    # Irises (darker shadow)
    cv2.circle(img, (center[0] - 80, center[1] - 50), 20, (0, 0, 0), -1)
    cv2.circle(img, (center[0] + 80, center[1] - 50), 20, (0, 0, 0), -1)
    
    # Mouth (distorted grimace, slightly hidden)
    cv2.ellipse(img, (center[0], center[1] + 50), (80, 30), 0, 0, 180, (255, 255, 255), -1)
    cv2.ellipse(img, (center[0], center[1] + 50), (80, 30), 0, 0, 180, (0, 0, 0), 5)

    # Apply Gaussian blur to make it subtle and eerie
    img = cv2.GaussianBlur(img, (75, 75), 30)
    
    return img

# Generate the hidden basilisk glare
hidden_basilisk = generate_hidden_basilisk(size)

# Blend the hidden basilisk into the existing op-art-noise background
final_basilisk_image = cv2.addWeighted(final_image, 0.85, hidden_basilisk, 0.15, 0)

# Display the final image
plt.figure(figsize=(6, 6))
plt.imshow(final_basilisk_image)
plt.axis("off")
plt.title("The Basilisk Glare - Hidden Infohazard")
plt.show()
