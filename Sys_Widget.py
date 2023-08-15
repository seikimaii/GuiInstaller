from PySide2 import QtWidgets, QtCore, QtGui

class Sys_Widget(QtWidgets.QWidget):
    def __init__(self):
        super(Sys_Widget, self).__init__()
        
        GridLayout = QtWidgets.QGridLayout()


        self.outputDir_path = '.'
        self.lineEdit_output_path = QtWidgets.QLineEdit()
        self.pushButton_browserPath = QtWidgets.QPushButton("Browse")

        self.pushButton_Execute = QtWidgets.QPushButton("Run")


        GridLayout.addWidget(self.lineEdit_output_path, 0, 0, 1, 6)
        GridLayout.addWidget(self.pushButton_browserPath, 0, 7, 1, 3)

        GridLayout.addWidget(self.pushButton_Execute, 2, 2, 1, 4)


        self.setLayout(GridLayout)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    win = Sys_Widget()
    win.show()

    sys.exit(app.exec_())