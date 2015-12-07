import psutil
from bitarray import bitarray
from entropy_class import entropy


class mem_entropy(entropy):
    def __init__(self):
        self.cur = psutil.virtual_memory()[3]
        super(mem_entropy, self).__init__()

    def _collect_entropy(self):
        collection = bitarray()
        for i in range(1000):
            val = psutil.virtual_memory()[3]
            if val != self.cur:
                self.cur = val
                collection.append((self.cur >> 3) & 1)
        self.entropy = self._unbias(collection)


def test():
    pass


if __name__ == '__main__':
    test()


