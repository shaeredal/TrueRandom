from sound_entropy import sound_entropy
from Crypto.Cipher import AES
import time

class true_rng:
    def __init__(self):
        self.collector = sound_entropy()
        self.bytes = self.collector.get_bytes()
        self.cur = 0

    def _get_byte(self):
        #while True:
        #    for byte in self.bytes:
        #        print(byte)
        #        yield byte
        #    self.collector.collect()
        #    self.bytes = self.collector.get_bytes()
        if len(self.bytes) == self.cur:
            self.collector.collect()
            self.bytes = self.collector.get_bytes()
            self.cur = 0
        self.cur += 1
        return self.bytes[self.cur - 1]


    def _get_value(self):
        pass


    def get_number(self, start = 0, end = 0):
        if end == 0 and start != 0:
            end = start
            start = 0
        if end < start:
            raise Exception('wrong parameters')

        val = (self._get_byte())
        ran = end - start
        return (val % ran) + start


def test():
    tr = true_rng()
    #for byte in tr._get_byte():
    #    print(byte)
    print(len(tr.bytes))
    while True:
        print(tr.get_number(14))
        #time.sleep(1)

if __name__ == '__main__':
    test()
    
