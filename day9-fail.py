# My first attempt was overengineered. It was pretty obvious that recursion was needed, but somehow I ended up here.

import numpy as np

def calculate_next_value(testsequence):
    i = 0
    f_steps = 2
    level = 0
    levels = [[x for x in testsequence]]
    polynominal_level = None
    for sec in range(0, 100):
        if len(levels) <= level+1:
            levels.append([])
        for l in range(0, level+1):
            for i in range(0, f_steps - l):
                levels[l+1].extend([0] * (f_steps - l - len(levels[l+1])))
                levels[l+1][i] = (abs(levels[l][i+1] - levels[l][i]))
        level += 1
        f_steps += 1
        if f_steps >= len(levels[0]):
            break
        if levels[-1][0] == 0:
            polynominal_level = len(levels)
        if polynominal_level is not None:
            break

    if polynominal_level is None:
        if len(levels[-1]) > 1 and len(list(set(levels[-1]))) == 1:
            polynominal_level = len(levels)
        else:
            return None

    y = np.array(levels[0])
    x = np.array(range(1, len(y) + 1))

    coefficients = np.polyfit(x, y, polynominal_level-1)

    polynomial = np.poly1d(coefficients)

    return round(polynomial(len(levels[0])+1))


with open("day9-alptbz.txt", "r") as fp:
    lines_raw = fp.readlines()

for line in lines_raw:
    next_value = None
    for t in range(0, 15):
        parts = [int(x) for x in line.strip().split(" ")]
        next_value = calculate_next_value(parts[t:])
        if next_value is not None:
            print(next_value)
            break
    if next_value is None:
        print(f'No value found for {line.strip()}')