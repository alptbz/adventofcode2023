import re

with open("day1-alptbz.txt", "r") as fp:
    inputlines = fp.readlines()

calibration_sum = 0

for input_line in inputlines:
    #all_digits_in_str = re.findall(r'\d', input_line)
    all_digits_in_str = []
    for c in input_line:
        if c.isdigit():
            all_digits_in_str.append(c)
    two_digit_num = int(all_digits_in_str[0] + all_digits_in_str[-1])
    calibration_sum += two_digit_num

print(f"Part One: {calibration_sum}")

