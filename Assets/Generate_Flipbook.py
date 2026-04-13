import glob
import os
from PIL import Image

# For Spread Logic
tempX = 0
tempY = 0

# Vars that will be used from our txt
extracted_vars = []
# txt location
file_path = './Settings.txt'

# Get All Sprite Images
png_files = glob.glob(os.path.join("./SpriteSheets", '*.*'))

# Set Output Path
output_path = "./Flipbook.png"

try:

    # Open our txt
    with open(file_path, 'r') as file:
        
        # Read line by line
        for line in file:
            # Clear spaces + clear \n then turn into array using split
            line = line.replace(" ", "").replace("\n", "").split("=")
            # Take array [1] because [0] is the name
            extracted_vars.append(line[1])

except FileNotFoundError:
    print("Error: Settings.txt was not found.")


Columns = int(extracted_vars[1])
Rows = int(extracted_vars[2])

# Check If Dynamic Rows is enabled
if int(extracted_vars[0]) == 1:

    # Resets Rows because we no longer need the var above
    Rows = 0

    # Start Looking For The Correct Row Value
    while len(png_files) > Rows * Columns:
        Rows = Rows + 1

# Get Sprite Size
Sprite_X, Sprite_Y = Image.open(png_files[0]).size

# Know the total size of our Flipbook then create an empty image
Flipbook_Size = [Sprite_X * Columns, Sprite_Y * Rows]
Flipbook_Image = Image.new("RGBA", Flipbook_Size, "#ff000000")

for png in png_files:
    
    # Open the image
    Sprite = Image.open(png)

    # paste our sprite to the flipbook image (we multiply with tempX/Y because these are the locations of our pasted sprite)
    # Note: even alpha paste over RGB so if there's alpha value, it will replace RGB value into alpha
    Flipbook_Image.paste(Sprite, (Sprite_X * tempX, Sprite_Y * tempY))

    # Spread Logic
    if tempX < Columns - 1:

        tempX = tempX + 1
    else:
        tempX = 0
        tempY = tempY + 1
    
# Save our image
Flipbook_Image.save(output_path)