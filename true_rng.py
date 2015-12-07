from sound_entropy import sound_entropy
#from mem_entropy import mem_entropy
from mouse_entropy import mouse_entropy


class true_rng:
    def __init__(self, collector):
        self.collector = collector
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
        b_int = []
        for b in range(4):
            b_int.append(self._get_byte())
        return int.from_bytes(b_int, byteorder='big')


    def get_number(self, start = 0, end = 0):
        if end == 0 and start != 0:
            end = start
            start = 0
        if end < start:
            raise Exception('wrong parameters')

        val = self._get_value()
        ran = end - start
        return (val % ran) + start


def test():
    tr = true_rng(mouse_entropy())
    #for byte in tr._get_byte():
    #    print(byte)
    #print(len(tr.bytes))
    #import time
    while True:
        print(tr.get_number(200, 400))
        #time.sleep(1)
    #import StatisticWindow
    #StaticWindow.histogramm([tr.get_number(300) for i in range(1000)])

if __name__ == '__main__':
    test()
    
