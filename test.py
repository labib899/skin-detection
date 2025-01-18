import imageio.v2 as imageio
import matplotlib.pyplot as plt
import numpy as np
import time

# Loading
#result_array = np.load("result_array.npy")
result_array = [[ [0 for col in range(256)] for col in range(256)] for row in range(256)]
with open("./result.array", "r") as file:
  for i in range(256):
    for j in range(256):
      for k in range(256):
        probability = file.readline()
        result_array[i][j][k] = float(probability)
print('data collected!')
# Testing
test_image_name = "pexels-photo-3806244.jpeg"
test_image = imageio.imread(test_image_name)
height, width, channel = test_image.shape

start=time.time()

for x in range(height):
  for y in range(width):
    b=test_image[x][y][0]
    g=test_image[x][y][1]
    r=test_image[x][y][2]

    if abs(result_array[r][g][b]) < 0.4:
      test_image[x][y][0] = 255
      test_image[x][y][1] = 255
      test_image[x][y][2] = 255

end=time.time()
print(f"Total processing time: {end-start} seconds...")

plt.imshow(test_image)