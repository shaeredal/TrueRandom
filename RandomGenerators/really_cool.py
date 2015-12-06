import pyaudio
import struct
import bitarray

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 48000
INPUT_BLOCK_TIME = 0.0001
INPUT_FRAMES_PER_BLOCK = 4


pa = pyaudio.PyAudio()

stream = pa.open(format=FORMAT,
                 channels=CHANNELS,
                 rate=RATE,
                 input=True,
                 frames_per_buffer=INPUT_FRAMES_PER_BLOCK)


with open('entropy.txt', 'w') as f:
    b = bitarray.bitarray()
    for i in range(1000):
        block = stream.read(INPUT_FRAMES_PER_BLOCK)
        shorts = struct.unpack('4h', block)
        for val in shorts:
            print(val)
            bit = val & 1
            b.append(bit)
            print(bit)
            f.write('{0}\n'.format(bit))
    print(b)
    #for i in b:
    #    print(i)
    #print(b[0])
    print(type(b))
    bias = bitarray.bitarray()
    bias = [b[i] for i in range( 0 ,len(b),2) if b[i] != b[i+1]]
    with open('filtered.txt', 'w') as f:
        for i in bias:
            if i:
                f.write('1\n')
            else:
                f.write('0\n')
    print(bias)
    #print(b.tobytes())

