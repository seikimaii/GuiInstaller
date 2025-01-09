# from guiCompile import GuiInstaller
from PySide2 import QtWidgets
import os

class GuiFunctions:
    @staticmethod
    def BrowsingScriptFiles(cls):
        files = QtWidgets.QFileDialog.getOpenFileNames(cls, "File", '.', 'python scripts(*.py)')[:-1][0]
        for f in files:
            x = os.path.basename(f)
            cls.lineEdit_Location.append(x)
        # print(files)

