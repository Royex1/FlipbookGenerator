# Flipbook Generator
This is a free tool that lets you generate flipbook images from a given sprites/textures, this tool only works on Windows for now, it's not tested on Mac or Linux but I'm planning to add them in the future
## Table Of Content
- [Installation](#Installation)
- [Tutorial](#Tutorial)
- [License](#License)
## Installation
- Step 1: You need to have Python install in order to use the tool go to https://www.python.org/downloads/ to download it (My current Python version is 3.14)
  
- Step 2: Run " Install Requirements.bat " to install the required libraries that the tool need to run (Pillow and PyQT5)
  
## Tutorial

https://github.com/user-attachments/assets/e7bc52bf-0ac3-4b54-93ec-b29eca9aa65c

- To open the tool double click " GUI.bat "
  
- Source Folder is where you have your sprites/textures that you want the tool to turn into a single flipbook, use " ./ " then the folder name if you put the folder inside the tool project or you can put the full path to the folder you want to use
  
- Exported Image should have the location and name of the flipbook you want to be generated, no need to add the format
  
- Export Alpha check box is used to choose if you want alpha to be included or removed from your flipbook, if you choose with alpha, the output will be .png and if you turn it off, the output will be .jpg
  
- Dynamic Rows check box will save you the headache of calculating how many rows are required in order to have all sprites in the flipbook, if you turn it on, the tool will automatically choose the correct amount of rows depending on how much columns you put, if you turn it off, a manual Rows value will appear to fill it up
  
- Number Of Columns (X) is the max number of Columns you want to have before jumping to the next row (X is meant to help remind the user that this number will make the flipbook grow horizontally)
  
- Number of Rows (Y) is the max number of Rows you want to have (Y is meant to help remind the user that this number will make the flipbook grow vertically)
  
- Generate Flipbook button will generate your flipbook based on the sprites you gave it

## License
The tool is mainly under MIT License but the GUI uses PyQT5 which's why it has GPLv3 License as well.

to be more specific:
- " Generate_Flipbook.py " uses MIT License
- " GUI.py " uses GPLv3 License

So if you want to Modify/Distribute or sell the code while staying under MIT License just remove GUI.py and create your own GUI or your own method to run Generate_Flipbook.py

[MIT LICENSE](LICENSE)

[GPLv3 LICENSE](LICENSE-GPL)
