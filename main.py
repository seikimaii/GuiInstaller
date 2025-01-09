from PySide2 import QtWidgets, QtGui, QtCore
import sys, traceback, threading, time,io, subprocess
from Script_Widget import Script_Widget
from Sys_Widget import Sys_Widget
from PyInstaller import __main__ as pymain
from PyInstaller.log import logging
# import subprocess
# import logging
# import utils

logging.basicConfig(level=logging.DEBUG)
# logger = logging.getLogger(__name__)

class Worker(QtCore.QThread):
    update_signal = QtCore.Signal(str)
    data = ''
    def run(self):
        self.update_signal.emit(self.data)
        

class Forward(io.TextIOBase):
    output_str = ""
    def __init__(self, back):
        self.worker = back

    def write(self, string):
        if string:
            self.worker.data = string
            self.worker.start()
        
        return len(string)
    def readline(self, __size: int = ...) -> str:

        if self.output_str:
            return self.output_str[0]
        return "EOF"

    def readable(self) -> bool:

        if self.output_str:
            return True
        return super().readable()
    
    def fileno(self) -> int:

        return len(self.output_str)
        # return super().fileno()



class MainWindow(QtWidgets.QWidget):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Pyking")
        self.setStyleSheet("background-color:rgb(230, 230, 230)")
                           
        self.resize(1200, 800)

        font = QtGui.QFont()
        font.setPointSize(18)
        font.setFamily("Consolas")

        verticalLayout = QtWidgets.QVBoxLayout()

        self.script_page = Script_Widget() 
        self.sys_page = Sys_Widget()

        self.pyinstaller_logger = logging.getLogger('PyInstaller')
        # self.pyinstaller_logger.handlers
        
        
        # print("waiting for start...")
        
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

        self.sys_page.pushButton_Execute.clicked.connect(self._Compile)
        self.output_list = []

        self.backing_thread = Worker()
        self.backing_thread.update_signal.connect(self.updateText)
        # self.zero = Forward(self.backing_thread)
        # sys.stderr = sys.stdout
        # self.redirec = Forward(self.backing_thread)
        
        

    def start_thread(self):
        self.backing_thread.start()
    
    def updateText(self, text):
        if text:
            self.sys_page.textArea.append(text)
            self.sys_page.update()

    def _Compile(self):

        # self.start_thread()
        # print("Starting!", file=MainWindow.forward)
        # x = QtWidgets.QDialog()
        # texb = QtWidgets.QTextBrowser(x)
        handler = logging.StreamHandler(Forward(self.backing_thread))
        handler.setFormatter(logging.Formatter('%(relativeCreated)d %(levelname)s: %(message)s'))
        self.pyinstaller_logger.addHandler(handler)


        # self.start_thread()

        # try:
        # subprocess.Popen(["pyinstaller", "test.py"], stdout=self.zero, stderr=self.zero, text=True)
        compile_thread = threading.Thread(target=pymain.run, args=(["test.py"],))
        compile_thread.start()
        # process = subprocess.Popen(["pyinstaller", "test.py"], stdout=MainWindow.forward, stderr=MainWindow.forward, text=True, shell=True)

        # process.

        # pymain.run(["test.py"])
        # except Exception as e:
        #     with open("hehe.txt", "a") as f:
        #         traceback.print_exc(file=f)
        
        # else:
        #     with open("nice.txt", 'a') as f:
        #         f.write("OK everything done!")

        # process = subprocess.Popen(["pyinstaller", "test.py"], stdout=subprocess.PIPE, 
        #                  stderr=subprocess.PIPE, text=True)
    
        



if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    # app.exec_()
    
    sys.exit(app.exec_())
