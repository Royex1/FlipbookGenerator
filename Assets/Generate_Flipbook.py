import glob
import os
from PIL import Image

def Alpha(AlphaValue):
    if AlphaValue == "True":
        return "RGBA", ".png", "#ff000000"
    else:
        return "RGB", ".jpg", "#000000FF"


def generate_flipbook(SourceFolder,ExportLocation,Col,Rw,DynamicRows,ExportAlpha):
    # For Spread Logic
    tempX = 0
    tempY = 0

    # Get All Sprite Images
    imgs = glob.glob(os.path.join(str(SourceFolder), '*.*'))


    Columns = int(Col)
    Rows = int(Rw)

    # Check If Dynamic Rows is enabled
    if DynamicRows == "True":

        # Resets Rows because we no longer need the var above
        Rows = 0

        # Start Looking For The Correct Row Value
        while len(imgs) > Rows * Columns:
            Rows = Rows + 1

    # Get Sprite Size
    Sprite_X, Sprite_Y = Image.open(imgs[0]).size

    # Know the total size of our Flipbook then create an empty image
    Flipbook_Size = [Sprite_X * Columns, Sprite_Y * Rows]
    Flipbook_Image = Image.new(Alpha(ExportAlpha)[0], Flipbook_Size, Alpha(ExportAlpha)[2])

    for img in imgs:
        
        # Open the image
        Sprite = Image.open(img)

        # paste our sprite to the flipbook image (we multiply with tempX/Y because these are the locations of our pasted sprite)
        # Note: even alpha paste over RGB so if there's alpha value, it will replace RGB value into alpha
        if ExportAlpha == "True":
            Flipbook_Image.paste(Sprite, (Sprite_X * tempX, Sprite_Y * tempY))
        else:
            Flipbook_Image.paste(Sprite, (Sprite_X * tempX, Sprite_Y * tempY), Sprite)
        # Spread Logic
        if tempX < Columns - 1:

            tempX = tempX + 1
        else:
            tempX = 0
            tempY = tempY + 1
        
    # Save our image
    Flipbook_Image.save(ExportLocation + Alpha(ExportAlpha)[1])