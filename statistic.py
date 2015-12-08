import pylab as plt
from collections import Counter


def histogramm(numbers, bins_count=10, name=""):
    """Рисует гистограмму значений и относительных частот

    numbers - последовательность
    bins_count - количество столбиков
    name - название графика
    """
    plt.subplot(2, 1, 1)
    plt.hist(numbers, bins=bins_count, normed=True)
    plt.title(name)
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.grid(True)


def variance_function(numbers):
    """Рисует график произвольных отклонений

    numbers - последовательность
    """
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
    plt.plot(range(len(y_list)), [0 for y in range(len(y_list))], 'r')
    plt.grid(True)


def noise(numbers):
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


def to_bits(numbers):
    bits = []
    string = ""
    for n in numbers:
        bits.append(bin(n)[2:])
    for n in bits:
        string += n
    string = [int(s) for s in string]
    return string


def load_file(file_name):
    with open(file_name, 'r') as f:
        arr = f.readlines()
    arr = [int(x) for x in arr]
    return arr


def display(nums, entropy):
    """Для вывода на экран всего что нарисовано

    вызывается последним
    """
    variance_function(entropy)
    histogramm(nums)
    noise(nums)
    plt.show()
