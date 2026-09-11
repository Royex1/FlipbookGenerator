from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys

import Generate_Flipbook as gf

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(800, 400, 350, 230)
        self.setWindowTitle("Flipbook Generator")
        self.extracted_vars = []
        self.initUI()

    def initUI(self):

        # Source Folder -------------------------------------------------------------
        self.SourceLabel = QtWidgets.QLabel(self)
        self.SourceLabel.setText("Source Folder:")
        self.SourceLabel.move(20,20)
        self.SourceLabel.adjustSize()

        self.SourceTextBox = QtWidgets.QLineEdit(self)
        self.SourceTextBox.setPlaceholderText("Put Folder Location")
        self.SourceTextBox.setText("./Sprites")        
        self.SourceTextBox.move(120,16)
        self.SourceTextBox.setFixedSize(200,25)

        # Exported Folder -------------------------------------------------------------
        self.ExportedLabel = QtWidgets.QLabel(self)
        self.ExportedLabel.setText("Exported Image:")
        self.ExportedLabel.move(20,50)
        self.ExportedLabel.adjustSize()

        self.ExportedTextBox = QtWidgets.QLineEdit(self)
        self.ExportedTextBox.setPlaceholderText("Image Location And Name")
        self.ExportedTextBox.setText("./Flipbook")        
        self.ExportedTextBox.move(120,46)
        self.ExportedTextBox.setFixedSize(200,25)


        # Export Alpha -------------------------------------------------------------
        self.AlphaLabel = QtWidgets.QLabel(self)
        self.AlphaLabel.setText("Export Alpha")
        self.AlphaLabel.move(20,90)
        self.AlphaLabel.adjustSize()

        self.AlphaBox = QtWidgets.QCheckBox(self)
        self.AlphaBox.setCheckState(2)
        self.AlphaBox.move(110,90)
        self.AlphaBox.adjustSize()


        
        # Dynamic Rows -------------------------------------------------------------
        self.DynamicRowLabel = QtWidgets.QLabel(self)
        self.DynamicRowLabel.setText("Dynamic Rows")
        self.DynamicRowLabel.move(20,120)
        self.DynamicRowLabel.adjustSize()

        self.DynamicRowBox = QtWidgets.QCheckBox(self)
        self.DynamicRowBox.setCheckState(2)
        self.DynamicRowBox.stateChanged.connect(self.UpdateGUI)
        self.DynamicRowBox.move(110,120)
        self.DynamicRowBox.adjustSize()



        # Columns X ---------------------------------------------------------------------
        self.ColumnLabel = QtWidgets.QLabel(self)
        self.ColumnLabel.setText("Number Of Columns (X)")
        self.ColumnLabel.move(20,155)
        self.ColumnLabel.adjustSize()

        self.ColumnBox = QtWidgets.QSpinBox(self)
        self.ColumnBox.setRange(0,1000)
        self.ColumnBox.setValue(3)
        self.ColumnBox.move(170,154)
        self.ColumnBox.adjustSize()



        # Rows Y ---------------------------------------------------------------------
        self.RowLabel = QtWidgets.QLabel(self)
        self.RowLabel.setText("Number Of Rows (Y)")
        self.RowLabel.move(10000,190)
        self.RowLabel.adjustSize()

        self.RowBox = QtWidgets.QSpinBox(self)
        self.RowBox.setRange(0,1000)
        self.RowBox.setValue(3)
        self.RowBox.move(10000,189)
        self.RowBox.adjustSize()



        #Buttones
        self.generateButton = QtWidgets.QPushButton(self)
        self.generateButton.setText("Generate Flipbook")
        self.generateButton.clicked.connect(self.generateFlipbook)
        self.generateButton.move(20,190)
        self.generateButton.adjustSize()



    # Generate Images

    def generateFlipbook(self):
        
        gf.generate_flipbook(self.SourceTextBox.text(), 
                             self.ExportedTextBox.text(), 
                             str(self.ColumnBox.value()), 
                             str(self.RowBox.value()), 
                             str(self.DynamicRowBox.isChecked()), 
                             str(self.AlphaBox.isChecked()))

    def UpdateGUI(self):
        if self.DynamicRowBox.checkState() == 2:
            self.RowLabel.move(10000,190)
            self.RowBox.move(10000,189)
            self.generateButton.move(20,190)
            self.resize(350, 230)
        else:
            self.RowLabel.move(20,190)
            self.RowBox.move(150,189)
            self.generateButton.move(20,220)
            self.resize(350, 260)



def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()