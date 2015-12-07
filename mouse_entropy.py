from tkinter import *
from bitarray import bitarray
from entropy_class import entropy


class mouse_entropy(entropy):

    def __init__(self):
        super(mouse_entropy, self).__init__()


    def _collect_entropy(self):
        vs = Tk()
        collection = bitarray()
        prev = vs.winfo_pointerxy()
        i = 0
        while i < 4000:
            cur = vs.winfo_pointerxy()
            if cur != prev:
                i += 1
                prev = cur

                x = vs.winfo_pointerxy()[0] & 1
                y = vs.winfo_pointerxy()[1] & 1

                collection.append(x ^ y)
                print(collection[-1])
        vs.destroy()
        self.entropy = self._unbias(collection)


def test():
    #import StatisticWindow as sw
    me = mouse_entropy()
    print(len(me.get_bytes()))
    #sw.display(list(me.get_bytes()))


if __name__ == '__main__':
    test()
