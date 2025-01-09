import logging
import time

class TextBrowserHandler(logging.Handler):
    def __init__(self, text_browser):
        super().__init__()
        self.text_browser = text_browser
        self.n = 0
        self.setLevel(logging.DEBUG)
    def emit(self, record):
        tm = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(record.created))
        
        msg = record.msg
        # if record.levelname == 'INFO':
        #     text =f'''<p>{tm} <span>{record.levelname}</span> : {msg}</p>''' 
        # elif record.levelname == 'DEBUG':
        #     pass
        # elif record.levelname == 'WARNING':
        #     text =f'''<p>{tm} <span style="color:#eb2d2d">{record.levelname}</span> : {msg}</p>'''
        # elif record.levelname == 'CRITICAL':
        #     text =f'''<p>{tm} <span style="color:#FF0000">{record.levelname}</span> : {msg}</p>'''
        # elif record.levelname == 'ERROR':
        #     text =f'''<p>{tm} <span style="color:#CC0000">{record.levelname}</span> : {msg}</p>'''
        # else:
        #     text = msg

        self.text_browser.append(msg)
        self.text_browser.append(str(self.n))
        self.n += 1