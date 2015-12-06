import pyaudio
import struct
import bitarray


class sound_entropy:

    def __init__(self):
        pa = pyaudio.PyAudio()

        self.stream = pa.open(format=pyaudio.paInt16,
                         channels=1,
                         rate=48000,
                         input=True,
                         frames_per_buffer=4)

        self.entropy = bitarray.bitarray()
        self._collect_entropy()
        self._unbias()


    def _collect_entropy(self):
        for i in range(1000):
            block = self.stream.read(4)
            shorts = struct.unpack('4h', block)
            for val in shorts:
                bit = val & 1
                self.entropy.append(bit)


    def _unbias(self):
        self.entropy = bitarray.bitarray([self.entropy[i] for i in range( 0 ,len(self.entropy),2)\
         if self.entropy[i] != self.entropy[i+1]])


    def get_entropy(self):
        return self.entropy


    def get_bytes(self):
        return self.entropy.tobytes()


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
    se.write_bin_in_text_file('filtered.txt')




if __name__ == '__main__':
    test()


