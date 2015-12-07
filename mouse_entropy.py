from tkinter import *
import bitarray
from operator import xor

p = Tk()


class mouse_entropy(object):

    def __init__(self):
        self.random_bits = bitarray.bitarray()

    def get_list(self):
        nums = []
        for val in self.random_bits:
                if val:
                    nums.append(1)
                else:
                    nums.append(0)
        return nums

    def get_random_bits(self, num):
        global p
        prev = p.winfo_pointerxy()
        i = 0
        while i != num:
            if p.winfo_pointerxy() != prev:
                i += 1
                prev = p.winfo_pointerxy()

                x = bin(p.winfo_pointerxy()[0])
                y = bin(p.winfo_pointerxy()[1])

                x = int(x[-1:])
                y = int(y[-1:])

                res_bit = xor(x, y)
                self.random_bits.append(res_bit)
                print(self.random_bits[-1])
        p.destroy()
        return self.random_bits

    def get_bytes(self):
        return self.random_bits.tobytes()

    def write_bin_in_text_file(self, filename):
        with open(filename, 'w') as f:
            for val in self.random_bits:
                if val:
                    f.write('1\n')
                else:
                    f.write('0\n')

if __name__ == '__main__':
    import statistic as sw
    me = mouse_entropy()
    me.get_random_bits(3000)
    sw.display(list(me.get_bytes()))
