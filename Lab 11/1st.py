from PIL import Image
import numpy as np
img = Image.open(r'F:\SEMESTER\python\MU.jpg')
img_array = np.array(img)

h, w = img_array.shape[0], img_array.shape[1]
print(f"Image size: {h} x {w}")

print(f"Image shape: {img_array.shape}")

min_blue = img_array[:, :, 2].min()
print(f"Lowest Blue value: {min_blue}")