from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
img = Image.open(r'F:\SEMESTER\python\MU.jpg')
data = np.array(img)   

red = data[:, :, 0]
green = data[:, :, 1]
blue = data[:, :, 2]

plt.figure(figsize=(10, 5))

plt.subplot(1, 4, 1)
plt.imshow(img)
plt.title("Original")
plt.axis("off")

plt.subplot(1, 4, 2)
plt.imshow(red, cmap='Reds')
plt.title("Red")
plt.axis("off")

plt.subplot(1, 4, 3)
plt.imshow(green, cmap='Greens')
plt.title("Green")
plt.axis("off")

plt.subplot(1, 4, 4)
plt.imshow(blue, cmap='Blues')
plt.title("Blue")
plt.axis("off")

plt.show()

