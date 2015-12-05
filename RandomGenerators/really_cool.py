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
    for i in range(1000):
        block = stream.read(INPUT_FRAMES_PER_BLOCK)
        shorts = struct.unpack('4h', block)
        for val in shorts:
            print(val)
            f.write('{0}\n'.format(val & 1))
