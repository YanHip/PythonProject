from queue import Queue
from threading import Thread
import time
import logging
import random

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s', )
item = Queue(100)


class Producer(Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, verbose=None):
        super(Producer, self).__init__()
        self.name = name

    def wait(self):
        time.sleep(random.random())

    def produce_item(self, i):
        if not item.full():
            # number = random.randint(1, 10)
            item.put(self.name +' message :' + str(i))
            logging.debug('Putting')
            self.wait()

    def run(self):
        i = 0
        while i < 20:
            self.produce_item(i)
            i += 1
        return


class Consumer(Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, verbose=None):
        super(Consumer, self).__init__()
        self.name = name
        return

    def wait(self):
        time.sleep(random.random())

    def consum_item(self):
        if not item.empty():
            get = item.get()
            logging.debug('Getting ' + str(get))
            self.wait()

    def run(self):
        while True:
            self.consum_item()
        return



if __name__ == '__main__':
    for i in range(3):
        threadProd = Producer(name='producer'+str(i))
        threadProd.start()
        # time.sleep(2)

    for i in range(3):
        threadCons = Consumer(name='consumer'+str(i))
        threadCons.start()
        # time.sleep(2)

    # time.sleep(2)
    # pour test
    # threadCons.start()
    # time.sleep(2)
    # threadProd.start()
    # time.sleep(2)


