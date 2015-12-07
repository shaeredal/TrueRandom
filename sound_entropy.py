import pyaudio
import struct
from bitarray import bitarray
from entropy_class import entropy


class sound_entropy(entropy):

    def __init__(self):
        pa = pyaudio.PyAudio()

        self.stream = pa.open(format=pyaudio.paInt16,
                              channels=1,
                              rate=48000,
                              input=True,
                              frames_per_buffer=4)

        super(sound_entropy, self).__init__()

    def _collect_entropy(self):
        collection = bitarray()
        for i in range(1000):
            block = self.stream.read(4)
            shorts = struct.unpack('4h', block)
            for val in shorts:
                collection.append(val & 1)
        self.entropy = self._unbias(collection)


def test():
    se = sound_entropy()
    print(se.get_entropy())
    print(se.to_bin_list())


if __name__ == '__main__':
    test()
