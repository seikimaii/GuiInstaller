from PySide2 import QtWidgets, QtCore, QtGui
import os

class GuiInstaller(QtWidgets.QScrollArea):
    def __init__(self):
        super(GuiInstaller, self).__init__()
        self.setWindowTitle("Pyking")
        self.resize(1000, 800)

        GridLayout = QtWidgets.QGridLayout()

        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(15)

        self.label_title = QtWidgets.QLabel("Script Location")
        self.label_title.setFixedHeight(60)
        self.label_title.setFont(font)

        self.listWidget_source = QtWidgets.QListWidget()
        self.label_sourceNums = QtWidgets.QLabel("0 Files")
        self.label_sourceNums.setFont(font)
        self.pushButton_browsingFiles = QtWidgets.QPushButton('Browse')
        self.pushButton_browsingFiles.clicked.connect(self._showSourceFiles)


        self.frame_packingType = QtWidgets.QFrame()
        self.frame_packingType.setFrameStyle(1)
        gridlayout_packingType = QtWidgets.QGridLayout()
        
        self.label_packingType = QtWidgets.QLabel("Packing Type")
        self.label_packingType.setFixedHeight(60)
        self.label_packingType.setFont(font)

        self.radio_oneFile = QtWidgets.QRadioButton("One File")
        self.radio_oneFile.setAutoExclusive(False)
        self.radio_oneFile.setChecked(True)
        self.radio_oneFile.setAutoExclusive(True)
        self.radio_oneDir = QtWidgets.QRadioButton("One Dir")
        
        gridlayout_packingType.addWidget(self.label_packingType, 0, 0, 1, 2)
        gridlayout_packingType.addWidget(self.radio_oneFile, 1, 0, 1, 1)
        gridlayout_packingType.addWidget(self.radio_oneDir, 1, 1, 1, 1)
        self.frame_packingType.setLayout(gridlayout_packingType)

        self.frame_console = QtWidgets.QFrame() 
        self.frame_console.setFrameStyle(1)
        gridlayout_console = QtWidgets.QGridLayout()
        
        self.label_console = QtWidgets.QLabel("Console")
        self.label_console.setFixedHeight(60)
        self.label_console.setFont(font)
        self.radio_consoleHide = QtWidgets.QRadioButton("Hide")
        self.radio_consoleHide.setAutoExclusive(False)
        self.radio_consoleHide.setChecked(True)
        self.radio_consoleHide.setAutoExclusive(True)
        self.radio_consoleShow = QtWidgets.QRadioButton("Show")
        gridlayout_console.addWidget(self.label_console, 0, 0, 1, 2)
        gridlayout_console.addWidget(self.radio_consoleHide, 1, 0, 1, 1)
        gridlayout_console.addWidget(self.radio_consoleShow, 1, 1, 1, 1)
        self.frame_console.setLayout(gridlayout_console)

        self.label_addData = QtWidgets.QLabel("External Data")
        self.label_addData.setFixedHeight(60)
        self.label_addData.setFont(font)
        # self.textEdit_Data = QtWidgets.QTextEdit()
        self.listWidget_Data = QtWidgets.QListWidget()
        self.label_DataNums = QtWidgets.QLabel("0 Files")
        self.label_DataNums.setFont(font)
        self.pushButton_addDataItem = QtWidgets.QPushButton("Add")
        self.pushButton_addDataItem.clicked.connect(self._showDataFiles)

        self.pushButton_Execute = QtWidgets.QPushButton("Run")

        GridLayout.addWidget(self.label_title, 0, 0, 1, 10)
        GridLayout.addWidget(self.label_sourceNums, 0, 5, 1, 2)
        GridLayout.addWidget(self.listWidget_source, 1, 0, 1 ,10)
        GridLayout.addWidget(self.pushButton_browsingFiles, 0, 7, 1, 2)
        
        # GridLayout.addWidget(self.label_packingType, 2, 0, 1, 4)
        # GridLayout.addWidget(self.radio_oneFile, 3, 0, 1, 1)
        # GridLayout.addWidget(self.radio_oneDir, 3, 1, 1, 1)
        GridLayout.addWidget(self.frame_packingType, 2, 0, 2, 5)

        # GridLayout.addWidget(self.label_console, 2, 5, 1, 4)
        # GridLayout.addWidget(self.radio_consoleHide, 3, 5, 1, 1)
        # GridLayout.addWidget(self.radio_consoleShow, 3, 6, 1, 1)
        GridLayout.addWidget(self.frame_console, 2, 5, 2, 5)

        GridLayout.addWidget(self.label_addData, 6, 0, 1, 10)
        GridLayout.addWidget(self.label_DataNums, 6, 5, 1, 2)
        GridLayout.addWidget(self.listWidget_Data, 7, 0, 1, 10)
        GridLayout.addWidget(self.pushButton_addDataItem, 6, 7, 1, 2)

        GridLayout.addWidget(self.pushButton_Execute, 8, 3, 1, 4)

        self.setLayout(GridLayout)

        shortcut_source = QtWidgets.QShortcut(QtGui.QKeySequence.Delete, self.listWidget_source, None, None, QtCore.Qt.WidgetWithChildrenShortcut)
        shortcut_source.activated.connect(self.delete_list_item)
        
        shortcut_data = QtWidgets.QShortcut(QtGui.QKeySequence.Delete, self.listWidget_Data, None, None, QtCore.Qt.WidgetWithChildrenShortcut)
        shortcut_data.activated.connect(self.delete_list_item)


    def _showSourceFiles(self):
        files = QtWidgets.QFileDialog.getOpenFileUrls(filter="*.py")
        for f in files[0]:
            self.listWidget_source.addItem(QtWidgets.QListWidgetItem(f.toLocalFile()))
        
        self.label_sourceNums.setText(f"{len(files[0])} Files")

    def _showDataFiles(self):
        files = QtWidgets.QFileDialog.getOpenFileUrls(filter="Documents (*.ini *.log *.csv *.txt);;"
                                                       "All Files(*.*)""Images (*.png *.jpg *.jpeg);;")
        for f in files[0]:
            self.listWidget_Data.addItem(QtWidgets.QListWidgetItem(f.toLocalFile()))
        self.label_DataNums.setText(f"{len(files[0])} Files")
        
    def delete_list_item(self):
        
        if self.listWidget_source.hasFocus():
            listWidget = self.listWidget_source
            label_Nums = self.label_sourceNums
        elif self.listWidget_Data.hasFocus():
            listWidget = self.listWidget_Data
            label_Nums = self.label_DataNums
        else:
            return
        items = listWidget.selectedItems()
        for i in items:
            listWidget.takeItem(listWidget.row(i))

        label_Nums.setText(f"{listWidget.count()} Files")
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = GuiInstaller()
    ui.show()
    
    sys.exit(app.exec_())