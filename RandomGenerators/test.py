import random
with open('numbers.txt', 'w') as f:
    f.writelines('{}\n'.format(random.randint(0, 1)) for _ in range(50000))

with open('numbers.txt') as f:
    s = f.read().replace(' ', '')

with open('numbers.txt', 'w') as h:
    h.write(s)