import math


def calc_race(t_in, d_in):
    _t_min = math.ceil(0.5 * (t_in - math.sqrt(t_in ** 2 - 4 * d_in)))
    _t_max = math.floor(0.5 * (math.sqrt(t_in ** 2 - 4 * d_in) + t_in))
    return _t_min, _t_max, _t_max - _t_min + 1


with open("day6.txt", "r") as fp:
    lines_raw = fp.readlines()

times = list(map(int, [x.strip() for x in lines_raw[0].split(" ")[1:] if x.strip() != '']))
distances = list(map(int, [x.strip() for x in lines_raw[1].split(" ")[1:] if x.strip() != '']))
# PART ONE
num_options = 1

for i in range(0, len(times)):
    t_min, t_max, num_option = calc_race(times[i], distances[i])
    num_options = num_options * num_option

print(f'Part One: {num_options}')
# PART TWO
total_time = int("".join([str(x) for x in times]))
total_distance = int("".join([str(x) for x in distances]))

print(f'Part Two: {calc_race(total_time, total_distance)[2]}')




