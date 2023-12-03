import re

number_replacements = {"one": "one1one",
                       "two": "two2two", "three": "three3three", "four": "four4four",
                       "five": "five5five", "six": "six6six", "seven": "seven7seven",
                       "eight": "eight8eight", "nine": "nine9nine"}

with open("day1.txt", "r") as fp:
    adjustments_raw = fp.readlines()

_sum_of_nums_simple = 0

for adjustment in adjustments_raw:
    for replacement in number_replacements:
        adjustment = adjustment.replace(replacement, number_replacements[replacement])
    num_parts = re.findall(r'\d', adjustment)
    two_digit_number_str = num_parts[0] + num_parts[-1]
    two_digit_number = int(two_digit_number_str)
    _sum_of_nums_simple += two_digit_number


print(_sum_of_nums_simple)