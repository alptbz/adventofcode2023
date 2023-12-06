import math

with open("day6.txt", "r") as fp:
    lines_raw = fp.readlines()

times = list(map(int, [x.strip() for x in lines_raw[0].split(" ")[1:] if x.strip() != '']))
distances = list(map(int, [x.strip() for x in lines_raw[1].split(" ")[1:] if x.strip() != '']))


def calc_race(t_in, d_in):
    _t_min = 0.5 * (t_in - math.sqrt(t_in ** 2 - 4 * d_in))
    _t_max = 0.5 * (math.sqrt(t_in ** 2 - 4 * d_in) + t_in)
    _t_min = math.ceil(_t_min)
    _t_max = math.floor(_t_max)
    _num_option = _t_max - _t_min + 1
    return _t_min, _t_max, _num_option

num_options = 1

for i in range(0, len(times)):
    t_in = times[i]
    d_in = distances[i]
    t_min, t_max, num_option = calc_race(t_in, d_in)
    num_options = num_options * num_option

print(f'Part One: {num_options}')

total_time = int("".join([str(x) for x in times]))
total_distance = int("".join([str(x) for x in distances]))

_, _, opt2 = calc_race(total_time, total_distance)

print(f'Part Two: {opt2}')




