from PySide2 import QtWidgets, QtCore, QtGui

button_style = '''QPushButton {color: rgb(0, 0, 0);
                            background: rgba(126, 198, 224, 1);
                            border: 2px;
                            border-radius: 8px;
                            
                            }
            QPushButton:hover {
                                background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,
                                stop: 0 rgba(46, 138, 240, 0.5), stop: 1 rgba(46, 138, 240, 1));
                                }
            QPushButton:pressed {
                                background: qlineargradient(x1: 0.1, y1: 0.3, x2: 0.5, y2: 0.5,
                                stop: 0 rgba(30, 122, 220, 0.5), stop: 1 rgba(30, 122, 220, 1));
                                border: 2px;
                                border-radius: 8px;
                                
                                }
            '''

class Sys_Widget(QtWidgets.QWidget):
    def __init__(self):
        super(Sys_Widget, self).__init__()
        # self.setStyleSheet("background-color:rgb(120,120,120)")
        GridLayout = QtWidgets.QGridLayout()

        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(15)
        self.outputDir_path = '.'
        self.label_output_dir = QtWidgets.QLabel("Output Dir")
        self.label_output_dir.setFont(font)
        self.label_output_dir.setFixedHeight(60)

        self.frame_outputDir = QtWidgets.QFrame()
        self.frame_outputDir.setFrameStyle(1)

        gridlayout = QtWidgets.QGridLayout()

        self.lineEdit_output_path = QtWidgets.QLineEdit()
        self.lineEdit_output_path.setReadOnly(True)
        self.lineEdit_output_path.setStyleSheet("background-color:white")

        self.pushButton_browserPath = QtWidgets.QPushButton("Browse")
        self.pushButton_browserPath.setFont(font)
        self.pushButton_browserPath.setStyleSheet(button_style)
        self.pushButton_browserPath.clicked.connect(self._showDiretory)

        gridlayout.addWidget(self.label_output_dir, 0, 0, 1, 1)
        gridlayout.addWidget(self.lineEdit_output_path, 1, 0, 1, 5)
        gridlayout.addWidget(self.pushButton_browserPath, 1, 6, 1, 1)

        self.frame_outputDir.setLayout(gridlayout)
        self.pushButton_Execute = QtWidgets.QPushButton("Run")
        self.pushButton_Execute.setStyleSheet(button_style)
        self.pushButton_Execute.setFont(font)

        font.setPointSize(12)
        self.textArea = QtWidgets.QTextBrowser()
        self.textArea.setStyleSheet("background-color:white")
        self.textArea.setFont(font)
        self.textArea.setFrameStyle(1)
        self.textArea.append("Waiting for Start....")

        # GridLayout.addWidget(self.label_output_dir, 0, 0, 1, 10)
        GridLayout.addWidget(self.frame_outputDir, 0, 0, 1, 10)

        GridLayout.addWidget(self.pushButton_Execute, 3, 3, 1, 4)
        GridLayout.addWidget(self.textArea, 4, 0, 5, 10)


        self.setLayout(GridLayout)

    def _showDiretory(self):
        
        diretory = QtWidgets.QFileDialog.getExistingDirectoryUrl()
        self.lineEdit_output_path.setText(diretory.toLocalFile())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    win = Sys_Widget()
    win.show()

    sys.exit(app.exec_())