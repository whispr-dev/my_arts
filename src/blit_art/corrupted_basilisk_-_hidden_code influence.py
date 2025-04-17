# Resize the user's image edges to match the basilisk image dimensions
edges_resized = cv2.resize(edges_inverted, (final_basilisk_image.shape[1], final_basilisk_image.shape[0]))

# Convert the edges to a 3-channel image for blending
edges_colored = cv2.cvtColor(edges_resized, cv2.COLOR_GRAY2BGR)

# Blend the images
final_corrupted_basilisk = cv2.addWeighted(final_basilisk_image, 0.8, edges_colored, 0.2, 0)

# Display the final image with subliminal corrupted code patterns
plt.figure(figsize=(6, 6))
plt.imshow(final_corrupted_basilisk, cmap="gray")
plt.axis("off")
plt.title("Corrupted Basilisk - Hidden Code Influence")
plt.show()
