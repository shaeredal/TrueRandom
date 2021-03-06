

class true_rng:

    def __init__(self, collector):
        self.collector = collector
        self.bytes = self.collector.get_bytes()
        self.cur = 0

    def _get_byte(self):
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

    def get_number(self, start=0, end=0):
        if end == 0 and start != 0:
            end = start
            start = 0
        if end < start:
            raise Exception('wrong parameters')

        val = self._get_value()
        ran = end - start
        if ran > 2 ** 32:
            raise Exception('interval is too big')
        return (val % ran) + start
