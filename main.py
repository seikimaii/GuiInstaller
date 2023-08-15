from PySide2 import QtWidgets, QtGui
from Script_Widget import Script_Widget
from Sys_Widget import Sys_Widget

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Pyking")
        self.setStyleSheet("background-color:rgb(230, 230, 230)")
                           
        self.resize(800, 800)

        font = QtGui.QFont()
        font.setPointSize(18)
        font.setFamily("Consolas")

        verticalLayout = QtWidgets.QVBoxLayout()

        self.script_page = Script_Widget() 
        self.sys_page = Sys_Widget()
        
        self.tabWidget = QtWidgets.QTabWidget()
        self.tabWidget.setStyleSheet('''
                                        QTabWidget::pane {
                                                            border: none;
                                                            
                                                            }
                                        QTabBar::tab:selected {border-color:black; border-bottom:none;background-color:rgb(230,230,230)}
                                        QTabBar::tab {width:280px; height:60px; background-color:rgb(200,200,200); border-style:solid; border-width:1px; border-top-right-radius: 20px;border-top-left-radius: 20px}
                                    ''')
        self.tabWidget.setFont(font)
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
