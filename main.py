from PySide2 import QtWidgets
from Script_Widget import Script_Widget
from Sys_Widget import Sys_Widget

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Pyking")
        self.resize(800, 800)
        verticalLayout = QtWidgets.QVBoxLayout()

        self.script_page = Script_Widget() 
        self.sys_page = Sys_Widget()
        
        self.tabWidget = QtWidgets.QTabWidget()
        self.tabWidget.addTab(self.script_page, "Script")
        self.tabWidget.addTab(self.sys_page, "Sys Set")
        verticalLayout.addWidget(self.tabWidget)
        
        self.setLayout(verticalLayout)
        
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
