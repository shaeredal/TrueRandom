import pylab
from random import randint


def display_histogramm(rand_list, interval, name=""):
    """Отображение гистограммы равноинтервальным методом

    rand_list - список величин
    interval - интервал гистограммы
    name - название гистограммы

    """

    # rand_list.sort()
    i = 0
    partial_sum = 0
    partial_sum_list = []
    for item in rand_list:  # подсчет частичных сумм
        partial_sum += item
        i += 1
        if i == interval:
            partial_sum_list.append(partial_sum)
            partial_sum = 0
            i = 0

    print(partial_sum_list)
    y = [item/interval for item in partial_sum_list]  # высоты (y)
    print(y)

    x = []
    for _ in range(len(y)):  # подсчет интервалов (по x)
        i += 1
        x.append(interval * i)

    pylab.bar(x, y, interval)  # x - левый край столбца, y - высота
    if name != "":
        pylab.legend([name])
    pylab.grid(True)
    pylab.show()


def display_variance_function(rand_list):
    y = 0
    y_list = [0]
    for item in rand_list:
        if item == 1:
            y += 1
        else:
            y -= 1
        y_list.append(y)
    pylab.plot(y_list, 'b')
    pylab.plot(range(len(rand_list)), [0 for y in range(len(rand_list))], 'r')
    pylab.grid(True)
    pylab.show()


if __name__ == '__main__':
    lol = []
    with open('entropy.txt', 'r') as f:
        lol = f.readlines()
    lol = [int(x) for x in lol]
    print(lol)
    display_variance_function(lol)
