import threading
import time
from bitarray import bitarray
from entropy_class import entropy


class thread_entropy(entropy):

    def __init__(self):
        self.active = False
        self.ran_num = 0
        super(thread_entropy, self).__init__()

    def _adder(self):
        while self.active:
            time.sleep(0.0001)
            self.ran_num += 1
            if self.ran_num > 4000:
                self.ran_num = 0

    def _collect_entropy(self):
        threads = []
        self.active = True
        for i in range(8):
            threads.append(threading.Thread(target=self._adder))
            threads[i].start()
        collection = bitarray()
        for i in range(4000):
            time.sleep(0.0001)
            val = self.ran_num & 1
            collection.append(val)
        self.active = False
        self.entropy = self._unbias(collection)


def test():
    te = thread_entropy()
    print(te.get_entropy())
    print(len(te.get_bytes()))


if __name__ == '__main__':
    test()
