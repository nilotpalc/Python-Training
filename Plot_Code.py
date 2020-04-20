import matplotlib.pyplot as plt
from cmath import log
from math import pow

test_data = list(filter(
    lambda x: x != 0,
    [n / 100.0 for n in range(-1000, 1001)]))

equations = [
    (lambda x: 1),
    (lambda x: x),
    (lambda x: pow(x, 2)),
    (lambda x: pow(x, 3)),
    (lambda x: pow(x, 4)),
    (lambda x: log(x).real)
]

plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.xlim((-10, 10))
plt.ylim((-10, 10))

for equation in equations:
    plt.plot(test_data, list(map(equation, test_data)))

plt.show()

# Code copied from
# https://andy.stanton.is/writing/about/graphing-with-matplotlib/
