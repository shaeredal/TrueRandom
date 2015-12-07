from tkinter import *
from true_rng import true_rng
from mem_entropy import mem_entropy
from sound_entropy import sound_entropy
from mouse_entropy import mouse_entropy
from thread_entropy import thread_entropy
import statistic


root = Tk()
root.geometry("400x480+500+200")
bgc = '#1d1d1d'
fgc = '#d1d3d4'
btc = '#293955'
root.configure(bg=bgc)
root.title("Easy Random")


def get_params(tr):
    from_num = int(entry2.get())
    to_num = int(entry3.get()) + 1
    range_num = int(entry1.get())
    nums = [tr.get_number(from_num, to_num) for i in range(range_num)]

    text1.delete(1.0, END)
    text1.insert(INSERT, nums)

    statistic.display(nums)


def random_from_mouse():
    text1.insert(INSERT, 'Wait')
    tr = true_rng(mouse_entropy())
    get_params(tr)


def random_from_soundcard():
    tr = true_rng(sound_entropy())
    get_params(tr)


def random_from_threads():
    tr = true_rng(thread_entropy())
    get_params(tr)


def random_from_mem():
    tr = true_rng(mem_entropy())
    get_params(tr)

# сколько чисел
entry1 = Entry(root, font='Arial 9')
entry1.place(x=180, y=40, width=155)
label1 = Label(root, text='Number of values:', bg=bgc, fg=fgc, font='Arial 9')
label1.place(x=40, y=40, width=130)

# от
entry2 = Entry(root, font='Arial 9')
entry2.place(x=100, y=70, width=100)
label2 = Label(root, text='from', bg=bgc, fg=fgc, font='Arial 9')
label2.place(x=50, y=70, width=40)

# до
entry3 = Entry(root, font='Arial 9')
entry3.place(x=235, y=70, width=100)
label3 = Label(root, text='to', bg=bgc, fg=fgc, font='Arial 9')
label3.place(x=210, y=70, width=10)

# случайные величины
text1 = Text(root, height=9, width=7, wrap=WORD)
text1.pack(fill=X, padx=5, ipady=5, side=BOTTOM)

button1 = Button(root, text='Memory', command=random_from_mem, bg=btc, fg=fgc)
button2 = Button(root, text='Mouse move', command=random_from_mouse, bg=btc, fg=fgc)
button3 = Button(root, text='Soundcard', command=random_from_soundcard, bg=btc, fg=fgc)
button4 = Button(root, text='Threads', bg=btc, command=random_from_threads, fg=fgc)
label4 = Label(root, text='Get entropy from:', bg=bgc, fg=fgc, font='Arial 9')
button1.pack(fill=X, padx=5, ipady=5, side=BOTTOM)
button2.pack(fill=X, padx=5, ipady=5, side=BOTTOM)
button3.pack(fill=X, padx=5, ipady=5, side=BOTTOM)
button4.pack(fill=X, padx=5, ipady=5, side=BOTTOM)
label4.pack(fill=X, padx=5, ipady=5, side=BOTTOM)


entry1.insert(INSERT, '1000')
entry2.insert(INSERT, '0')
entry3.insert(INSERT, '1000')

root.mainloop()
