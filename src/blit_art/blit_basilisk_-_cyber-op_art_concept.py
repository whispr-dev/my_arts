import numpy as np
import matplotlib.pyplot as plt
import cv2

# Generate an op-art pattern inspired by the McCollough Effect
def generate_op_art_pattern(size=512):
    img = np.zeros((size, size, 3), dtype=np.uint8)
    step = size // 32  # Grid step size

    for y in range(0, size, step):
        for x in range(0, size, step):
            if (x // step) % 2 == (y // step) % 2:
                img[y:y+step, x:x+step] = [255, 0, 0]  # Red blocks
            else:
                img[y:y+step, x:x+step] = [0, 255, 255]  # Cyan blocks

    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Generate machine code text overlay (simulating malware snippets)
malware_code_snippets = [
    "E8 00 00 00 00 5D C3",  # Simple CALL-RET malware snippet
    "B8 04 00 00 00 BB 01 00",  # MOV instructions in x86 assembly
    "90 90 90 90 90 90",  # NOP sled (common in exploits)
    "EB FE",  # Infinite JMP loop
    "FF D0",  # CALL EAX (used in exploits)
]

# Create a noisy, glitch-like background inspired by the Ganzfeld Effect
def generate_noise_background(size=512):
    noise = np.random.randint(0, 255, (size, size), dtype=np.uint8)
    noise = cv2.GaussianBlur(noise, (5,5), 0)
    return cv2.applyColorMap(noise, cv2.COLORMAP_JET)

# Create the final composition
size = 512
op_art = generate_op_art_pattern(size)
noise_bg = generate_noise_background(size)

# Blend the op-art pattern with the noise
final_image = cv2.addWeighted(op_art, 0.6, noise_bg, 0.4, 0)

# Overlay malware snippets as glitchy-looking ASCII text
for i, code in enumerate(malware_code_snippets):
    cv2.putText(final_image, code, (10, 50 + i * 40), cv2.FONT_HERSHEY_SIMPLEX, 
                0.8, (0, 255, 0), 2, cv2.LINE_AA)

# Display the image
plt.figure(figsize=(6, 6))
plt.imshow(final_image)
plt.axis("off")
plt.title("BLIT Basilisk - Cyber-Op Art Concept")
plt.show()
