import pylab as plt
from random import randint
from collections import Counter


def histogramm(numbers, bins_count=10, name=""):
    """Рисует гистограмму значений и относительных частот

    numbers - последовательность
    bins_count - количество столбиков
    name - название графика
    """
    #plt.figure()
    plt.subplot(2, 2, 1)
    plt.hist(numbers, bins=bins_count, normed=True)
    plt.title(name)
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.grid(True)


def polygon(numbers):
    """Рисует полигон значений и относительных частот

    numbers - последовательность
    """
    plt.subplot(2, 2, 2)
    #plt.figure()
    c = Counter(numbers)
    vars = list(c.keys())
    freq = [0]
    for key in c.keys():
        freq.append(c[key]/len(numbers))
    freq = freq[:-1]
    plt.plot(vars, freq)
    plt.xlabel("Value")
    plt.ylabel("Frequency")


def variance_function(numbers):
    """Рисует график произвольных отклонений

    numbers - последовательность
    """
    #plt.figure()
    plt.subplot(2, 1, 2)
    y = 0
    y_list = [0]
    for item in numbers:
        if item == 1:
            y += 1
        else:
            y -= 1
        y_list.append(y)
    plt.plot(y_list, 'b')
    plt.plot(range(len(numbers)), [0 for y in range(len(numbers))], 'r')
    plt.grid(True)


def noize(numbers):
    """Рисует случайные величины на координатной плоскости,
    красные точки - точки которые уже встречались в последовательности
    синие точки - точки, с наименьшим отклонением

    numbers - последовательность
    """
    plt.figure()
    i = 0
    pairs = []

    for n in numbers:
        if i == len(numbers) - 2:
            break
        i += 1
        pairs.append((numbers[i], numbers[i+1]))

    counter = Counter(pairs)
    coord_list = []

    for x in counter:
        coord_list.append(x)
    for item in pairs:
        if counter[item] > 1:
            plt.plot(item[0], item[1], 'r.')
        elif (item[0]+1, item[1]) in coord_list:
            plt.plot(item[0], item[1], 'b.')
        elif (item[0]-1, item[1]) in coord_list:
            plt.plot(item[0], item[1], 'b.')
        elif (item[0], item[1]+1) in coord_list:
            plt.plot(item[0], item[1], 'b.')
        elif (item[0], item[1]-1) in coord_list:
            plt.plot(item[0], item[1], 'b.')
        elif (item[0]+1, item[1]+1) in coord_list:
            plt.plot(item[0], item[1], 'b.')
        elif (item[0]-1, item[1]-1) in coord_list:
            plt.plot(item[0], item[1], 'b.')
        elif (item[0]+1, item[1]-1) in coord_list:
            plt.plot(item[0], item[1], 'b.')
        elif (item[0]-1, item[1]+1) in coord_list:
            plt.plot(item[0], item[1], 'b.')
        else:
            plt.plot(item[0], item[1], 'g.')


def display():
    """Для вывода на экран всего что нарисовано

    вызывается последним
    """
    plt.show()

if __name__ == '__main__':
    lol = [randint(0, 100) for x in range(10000)]
    variance_function([randint(0, 1) for x in range(1000)])
    histogramm(lol, 20)
    polygon(lol)
    noize(lol)
    display()
