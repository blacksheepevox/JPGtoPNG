import sys
import os
from PIL import Image # From Pillow Module

# Grab first and second argument from cmd
image_folder = sys.argv[1]
output_folder = sys.argv[2]

# Check if New/ exists, if not create New
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Convert images to PNG and Clean JPG
for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{output_folder}{clean_name}.png', 'png')
    print('All done!')
