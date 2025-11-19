from PIL import Image
import matplotlib.pyplot as plt

# Load your image
img = Image.open('p1.7.figure.png').convert('L')  # grayscale

# Resize (optional, to reduce points)
img = img.resize((100, 100))

pixels = img.load()
width, height = img.size

x, y, colors = [], [], []

for j in range(height):
    for i in range(width):
        brightness = pixels[i,j]
        if brightness < 200:  # threshold to skip very light pixels (optional)
            x.append(i)
            y.append(height - j)  # flip y so plot is right side up
            colors.append(brightness)

#plt.style.use('dark_background')
plt.scatter(x, y, c=colors, cmap='gray', s=10)
plt.gca().invert_yaxis()  # match image orientation
plt.axis('off')
plt.show()
