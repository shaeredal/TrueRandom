import sys
import time
from ctypes import *

def MMSYSERR_NOERROR(value):
    if value !=  0 :
        raise Exception("Error while running winmm.dll function", value)
    return value
 
for funcname in ["waveInOpen", "waveInPrepareHeader",
                 "waveInAddBuffer", "waveInStart",
                 "waveInStop", "waveInReset",
                 "waveInUnprepareHeader", "waveInClose"]:
    vars()[funcname] = windll.winmm[funcname]
    vars()[funcname].restype = MMSYSERR_NOERROR


class WAVEFORMATEX(Structure):
    WAVE_FORMAT_PCM = 1
    _fields_ = [("wFormatTag", c_ushort),
                ("nChannels", c_ushort),
                ("nSamplesPerSec", c_uint),
                ("nAvgBytesPerSec", c_uint),
                ("nBlockAlign", c_ushort),
                ("wBitsPerSample", c_ushort),
                ("cbSize", c_ushort)]
 
    def __init__(self, samples=48000, bits=16, channels=1):
        self.wFormatTag = WAVEFORMATEX.WAVE_FORMAT_PCM
        self.nSamplesPerSec = samples
        self.wBitsPerSample = bits
        self.nChannels = channels
        self.nBlockAlign = self.nChannels*self.wBitsPerSample // 8
        self.nAvgBytesPerSec = self.nBlockAlign*self.nSamplesPerSec
        self.cbSize =  0 
 

class WAVEHDR(Structure):
    _fields_ = [("lpData", POINTER(c_char)),
                ("dwBufferLength", c_uint),
                ("dwBytesRecorded", c_uint),
                ("dwUser", c_uint), # User data dword or pointer
                ("dwFlags", c_uint),
                ("dwLoops", c_uint),
                ("lpNext", c_uint), # pointer reserved
                ("reserved", c_uint)] # pointer reserved
    def __init__(self, waveformat):
        self.dwBufferLength = waveformat.nAvgBytesPerSec
        self.lpData = create_string_buffer('\000' * self.dwBufferLength)
        self.dwFlags =  0

waveFormat = WAVEFORMATEX(samples=48000,bits=16)
waveBufferArray = [WAVEHDR(waveFormat) for i in range(3)]

WRITECALLBACK = WINFUNCTYPE(None, c_uint, c_uint, POINTER(c_uint), POINTER(WAVEHDR), c_uint)

def pythonWriteCallBack(HandleWaveIn, uMsg, dwInstance, dwParam1, dwParam2):
    MM_WIM_CLOSE = 0x3BF
    MM_WIM_DATA = 0x3C0
    MM_WIM_OPEN = 0x3BE
    if   uMsg == MM_WIM_OPEN:
        print("Open handle =" + HandleWaveIn)
    elif uMsg == MM_WIM_CLOSE:
        print("Close handle =" + HandleWaveIn)
    elif uMsg == MM_WIM_DATA:
        #print "Data handle =", HandleWaveIn
        wavBuf = dwParam1.contents
        if wavBuf.dwBytesRecorded >  0 :
            bits = [ord(wavBuf.lpData[i]) & 1 for i in range( 0 ,wavBuf.dwBytesRecorded,2)]
            # для 24 бит: заменить в конце 2 на 3 в предыдущей строке
            bias = [bits[i] for i in range( 0 ,len(bits),2) if bits[i] != bits[i+1]]
            bytes =  [chr(reduce(lambda v,b:v<<1|b,bias[i-8:i], 0 )) for i in range(8,len(bias),8)]
            rndstr = ''.join(bytes)
            #print bytes,
            sys.stdout.write(rndstr)
        if wavBuf.dwBytesRecorded == wavBuf.dwBufferLength:
            waveInAddBuffer(HandleWaveIn, dwParam1, sizeof(waveBuf))
        else:
            print("Releasing one buffer from" + dwInstance[ 0 ])
            dwInstance[ 0 ]-=1
    else:
        raise "Unknown message"


writeCallBack=WRITECALLBACK(pythonWriteCallBack)
try:
    ExitFlag = c_uint(3)
    HandleWaveIn = c_uint( 0 )
    WAVE_MAPPER = c_int(-1)
    WAVE_FORMAT_QUERY = c_int(1)
    CALLBACK_FUNCTION = c_int(0x30000)
 
    waveInOpen( 0 , WAVE_MAPPER, byref(waveFormat),  0 ,  0 , WAVE_FORMAT_QUERY)
    waveInOpen(byref(HandleWaveIn), WAVE_MAPPER, byref(waveFormat), writeCallBack, byref(ExitFlag), CALLBACK_FUNCTION)
 
    for waveBuf in waveBufferArray:
        waveInPrepareHeader(HandleWaveIn, byref(waveBuf), sizeof(waveBuf))
        waveInAddBuffer(HandleWaveIn, byref(waveBuf), sizeof(waveBuf))
 
    waveInStart(HandleWaveIn)
 
    while 1:
        time.sleep(1)
 
except KeyboardInterrupt:
    waveInReset(HandleWaveIn)
 
    while 1:
        time.sleep(1)
        if ExitFlag.value ==  0 :
            break
 
    for waveBuf in waveBufferArray:
        waveInUnprepareHeader(HandleWaveIn, byref(waveBuf), sizeof(waveBuf))
 
    waveInClose(HandleWaveIn)
