from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys

import Generate_Flipbook as gf

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(int(800), int(400), 230, 170)
        self.setWindowTitle("Flipbook Generator")
        self.extracted_vars = []
        self.initUI()

    def initUI(self):

        # Dynamic Rows -------------------------------------------------------------
        self.DynamicRowLabel = QtWidgets.QLabel(self)
        self.DynamicRowLabel.setText("Dynamic Rows")
        self.DynamicRowLabel.move(20,20)
        self.DynamicRowLabel.adjustSize()

        self.DynamicRowBox = QtWidgets.QCheckBox(self)
        self.DynamicRowBox.setCheckState(0)
        self.DynamicRowBox.move(110,20)
        self.DynamicRowBox.adjustSize()



        # Columns X ---------------------------------------------------------------------
        self.ColumnLabel = QtWidgets.QLabel(self)
        self.ColumnLabel.setText("Number Of Columns (X)")
        self.ColumnLabel.move(20,55)
        self.ColumnLabel.adjustSize()

        self.ColumnBox = QtWidgets.QSpinBox(self)
        self.ColumnBox.setRange(0,100)
        self.ColumnBox.setValue(3)
        self.ColumnBox.move(170,54)
        self.ColumnBox.adjustSize()



        # Rows Y ---------------------------------------------------------------------
        self.RowLabel = QtWidgets.QLabel(self)
        self.RowLabel.setText("Number Of Rows (Y)")
        self.RowLabel.move(20,90)
        self.RowLabel.adjustSize()

        self.RowBox = QtWidgets.QSpinBox(self)
        self.RowBox.setRange(0,100)
        self.RowBox.setValue(3)
        self.RowBox.move(150,89)
        self.RowBox.adjustSize()



        #Buttones
        self.generateButton = QtWidgets.QPushButton(self)
        self.generateButton.setText("Generate Flipbook")
        self.generateButton.clicked.connect(self.generateFlipbook)
        self.generateButton.move(50,125)
        self.generateButton.adjustSize()



    # Generate Images

    def generateFlipbook(self):
        finalValues = [str(self.ColumnBox.value()),
                       str(self.RowBox.value()),
                       str(self.DynamicRowBox.isChecked())]
        gf.generate_flipbook(finalValues)



def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()