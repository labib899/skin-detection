import imageio.v2 as imageio
import matplotlib.pyplot as plt
import numpy as np
import time

def divide(x,y):
  if y==0:
    return 0
  else:
    return x/y

# Training
skin_array = [[ [1 for col in range(256)] for col in range(256)] for row in range(256)]
nonskin_array = [[ [1 for col in range(256)] for col in range(256)] for row in range(256)]

image_count = 555
indices = ["%04d" % x for x in range(1000)]
for image_index in range(image_count):
    mask_img_name = "ibtd/Mask/"+str(indices[image_index])+".bmp"
    unmask_img_name = "ibtd/"+str(indices[image_index])+".jpg"

    mask_img = imageio.imread(mask_img_name)
    unmask_img = imageio.imread(unmask_img_name)
    height, width, channels = mask_img.shape

    for x in range(height):
      for y in range(width):
        b=mask_img[x][y][0]
        g=mask_img[x][y][1]
        r=mask_img[x][y][2]

        if r>250 and g>250 and b>250:
          b = unmask_img[x][y][0] 
          g = unmask_img[x][y][1] 
          r = unmask_img[x][y][2]
          #print(mask_img_name,image_index,r,g,b)
          nonskin_array[r][g][b] = nonskin_array[r][g][b] + 1
        else:
          skin_array[r][g][b] = skin_array[r][g][b] + 1

skin_sum = 0
nonskin_sum = 0
for x in range(256):
  for y in range(256):
    skin_sum = skin_sum + sum(skin_array[x][y])
    nonskin_sum = nonskin_sum + sum(nonskin_array[x][y])

result_array = [[ [0 for col in range(256)] for col in range(256)] for row in range(256)]
for x in range(256):
  for y in range(256):
    for z in range(256):
      skin_array[x][y][z] = skin_array[x][y][z] / skin_sum
      nonskin_array[x][y][z] = nonskin_array[x][y][z] / nonskin_sum
      result_array[x][y][z] = skin_array[x][y][z] / nonskin_array[x][y][z]

# Saving
#np.save("result_array.npy", result_array)
f = open("./result.array", 'w')
f.write("")
for i in range(256):
  for j in range(256):
    for k in range(256):
      probability = (skin_array[i][j][k] / skin_sum) / (nonskin_array[i][j][k] / nonskin_sum)
      f.write(str(probability) + "\n")
  print(".", end="")

f.close()