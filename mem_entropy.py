import psutil
import time
from bitarray import bitarray
from entropy_class import entropy


class mem_entropy(entropy):

    def __init__(self):
        self.cur = psutil.virtual_memory()[3]
        super(mem_entropy, self).__init__()

    def _collect_entropy(self):
        collection = bitarray()
        for i in range(4000):
            time.sleep(0.0001)
            val = psutil.virtual_memory()[3]
            if val != self.cur:
                print(bin(val))
                self.cur = val
                collection.append((self.cur >> 12) & 1)
                print(collection[-1])
        if len(collection) % 2 != 0:
            collection = collection[1:]
        self.entropy = self._unbias(collection)
