
def get_expanded_galaxy(_lines):
    line_length = len(_lines[0].strip())
    cols_with_galaxies = []
    rows_with_no_galaxies = []

    horizontally_expanded_galaxy = []

    for r, line in enumerate(_lines):
        line = line.strip()
        has_no_galaxy = True
        for c, symb in enumerate(line):
            if symb == "#":
                cols_with_galaxies.append(c)
                has_no_galaxy = False
        if has_no_galaxy:
            rows_with_no_galaxies.append(r)
            horizontally_expanded_galaxy.append("".join(["."]*line_length))
        horizontally_expanded_galaxy.append(line)

    cols_with_no_galaxies = list(set(range(0,line_length)) - set(cols_with_galaxies))

    expanded_galaxy = []

    for x in range(0, len(horizontally_expanded_galaxy)):
        line = horizontally_expanded_galaxy[x]
        new_line = ""
        for y in range(0, len(line)):
            if y in cols_with_no_galaxies:
                new_line += "."
            new_line += line[y]
        expanded_galaxy.append(new_line)

    return expanded_galaxy, cols_with_no_galaxies, rows_with_no_galaxies


def find_galaxies(_galaxy):
    _galaxies = []
    for r, line in enumerate(_galaxy):
        line = line.strip()
        for c, symb in enumerate(line):
            if symb == "#":
                _galaxies.append((r, c))
    return _galaxies


def crosses(from_col, to_col, no_galaxy_cols_or_lines):
    _cols = [from_col, to_col]
    _min_col = min(_cols)
    _max_col = max(_cols)
    cols_within_min_max = [x for x in no_galaxy_cols_or_lines if _min_col < x < _max_col]
    return len(cols_within_min_max)


with open('day11.txt') as f:
    lines = f.read().splitlines()

expanded_galaxy, cols_with_no_galaxies, rows_with_no_galaxies = get_expanded_galaxy(lines)

expanded_galaxies = find_galaxies(expanded_galaxy)
total_len_part_one = 0

while len(expanded_galaxies) > 0:
    galaxy = expanded_galaxies.pop()
    for other_galaxy in expanded_galaxies:
        distance = abs(galaxy[0] - other_galaxy[0]) + abs(galaxy[1] - other_galaxy[1])
        total_len_part_one += distance

print(f'Part One: {total_len_part_one}')

galaxies = find_galaxies(lines)
total_len_part_two = 0
galaxy_age_factor = 1000000 - 1

while len(galaxies) > 0:
    galaxy = galaxies.pop()
    for other_galaxy in galaxies:
        row_crosses = crosses(galaxy[0], other_galaxy[0], rows_with_no_galaxies) * galaxy_age_factor
        col_crosses = crosses(galaxy[1], other_galaxy[1], cols_with_no_galaxies) * galaxy_age_factor
        _row_galaxy_vals = [galaxy[0], other_galaxy[0]]
        _col_galaxy_vals = [galaxy[1], other_galaxy[1]]
        distance_rows = max(_row_galaxy_vals) + row_crosses - min(_row_galaxy_vals)
        distance_cols = max(_col_galaxy_vals) + col_crosses - min(_col_galaxy_vals)
        total_len_part_two += distance_rows + distance_cols


print(f'Part Two: {total_len_part_two}')