import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG)#, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
loger = logging.getLogger(__name__)
loger.setLevel(logging.DEBUG)
# lock = threading.Lock()

def pp():
    for i in range(3):
        # with lock:
        # logging.info(str(i))
        loger.info(str(i))
        time.sleep(1)

x = threading.Thread(target=pp)
x.start()
x.join()