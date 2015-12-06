import pyaudio
import struct
from bitarray import bitarray


class sound_entropy:

    def __init__(self):
        pa = pyaudio.PyAudio()

        self.stream = pa.open(format=pyaudio.paInt16,
                         channels=1,
                         rate=48000,
                         input=True,
                         frames_per_buffer=4)

        self.entropy = bitarray()
        self._collect_entropy()


    def _collect_entropy(self):
        collection = bitarray()
        for i in range(1000):
            block = self.stream.read(4)
            shorts = struct.unpack('4h', block)
            for val in shorts:
                bit = val & 1
                collection.append(bit)
        self.entropy = self._unbias(collection)


    def _unbias(self, collection):
        return bitarray([collection[i] for i in range( 0 ,len(collection),2) if collection[i] != collection[i+1]])


    def collect(self):
        self._collect_entropy()


    def get_entropy(self):
        return self.entropy


    def get_bytes(self):
        return self.entropy.tobytes()


    def to_bin_list(self):
        result = []
        for i in self.entropy.tolist():
            if i:
                result.append(1)
            else:
                result.append(0)
        return result


    def write_bin_in_text_file(self, filename):
        with open(filename, 'w') as f:
            for val in self.entropy:
                if val:
                    f.write('1\n')
                else:
                    f.write('0\n')

def test():
    se = sound_entropy()
    print(se.get_entropy())
    #print(se.get_bytes())
    #for i in se.get_bytes():
    #    print(i)
    #se.write_bin_in_text_file('filtered.txt')
    print(se.to_bin_list())



if __name__ == '__main__':
    test()


