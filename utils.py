
import io
from PySide2.QtCore import QCoreApplication, QEventLoop

class ForwardToFunctionStream(io.TextIOBase):
    def __init__(self, output_function=None):
        self.output_function = output_function

    def write(self, string):
        self.output_function(string)
        # QCoreApplication.processEvents(QEventLoop.ExcludeUserInputEvents)
        # scroll_bar = self.output_function.verticalScrollBar()
        # scroll_bar.setValue(scroll_bar.maximum())
        # self.output_function.update()
        # print("1234567098767809892364582735682374568374569238756")
        return len(string)


if __name__ == "__main__":

    gg = ForwardToFunctionStream(print)

    print(gg.fileno())