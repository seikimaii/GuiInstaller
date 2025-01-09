import sys
import threading
from utils import ForwardToFunctionStream
from PySide2 import QtWidgets, QtCore, QtGui

class ConsoleInterface(QtWidgets.QFrame):
    def __init__(self):
        super(ConsoleInterface, self).__init__()
        
        # self.setFrameStyle(1)
        self.text_browser = QtWidgets.QTextBrowser()
        self.text_browser.setFrameStyle(1)
        self.input_line = QtWidgets.QLineEdit()
        self.input_line.setStyleSheet("background-color:white")
        
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.text_browser)
        layout.addWidget(self.input_line)
        
        self.setLayout(layout)
        
        self.input_line.returnPressed.connect(self.handle_input)

        self.redirec_stream = ForwardToFunctionStream(self.text_browser)

        # self.stdout = sys.stdout
        # self.stderr = sys.stderr
        # self.stdin = sys.stdin
        # sys.stdout = self.redirec_stream
        # sys.stderr = self.redirec_stream
        # sys.stdin = self

        self.stdout = self.redirec_stream
        self.stderr = self.redirec_stream
        self.stdin = self


        
        self.input_queue = []
        self.input_event = threading.Event()
        self.input_thread = threading.Thread(target=self.input_listener)
        self.input_thread.setDaemon(True)
        self.input_thread.start()
        
    def __del__(self):
        sys.stdout = self.stdout
        sys.stderr = self.stderr

    def write(self, text):
        self.text_browser.moveCursor(self.text_browser.textCursor().End)
        self.text_browser.insertPlainText(text)
        self.text_browser.update()
    
    # def fileno(self):
    #     self.

    def handle_input(self):
        user_input = self.input_line.text()
        self.input_queue.append(user_input)
        self.input_line.clear()
        self.input_event.set()

    def input_listener(self):
        while True:
            self.input_event.wait()
            if self.input_queue:
                user_input = self.input_queue.pop(0)


                try:
                    # age = int(user_input)
                    self.stdin.write(user_input+"\n")
                    # print(age)
                    
                except Exception:
                    print("Please enter a valid age.")
                else:
                    # print("You typed:", user_input)
                    pass
            self.input_event.clear()

    def closeEvent(self, event):
        event.accept()

if __name__ == "__main__":


    app = QtWidgets.QApplication(sys.argv)
    window = ConsoleInterface()
    window.show()
    sys.exit(app.exec_())
