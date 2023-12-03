from typing import List


class Coordinate:

    def __init__(self, row:int, column:int):
        self.column = column
        self.row = row


class PartNumber:

    def __init__(self, num: int, start_pos: Coordinate, end_pos: Coordinate):
        self.end_pos = end_pos
        self.start_pos = start_pos
        self.num = num
        self.symbol:PartSymbol = None

    def row(self):
        return self.start_pos.row

    def start_col(self):
        return self.start_pos.column

    def end_col(self):
        return self.end_pos.column

    def __str__(self):
        return f'{self.num}@R{self.start_pos.row} C{self.start_pos.column}-{self.end_pos.column}'

    def __repr__(self):
        return self.__str__()


class PartSymbol:

    def __init__(self, symbol: str, position: Coordinate):
        self.position = position
        self.symbol = symbol.strip()
        self.part_numbs: List[PartNumber] = []

    def in_range(self, row: int, col_start: int, col_end: int):
        in_row = row - 1 <= self.position.row <= row + 1
        in_column = col_start - 1 <= self.position.column <= col_end
        return in_row and in_column

    def link_part(self, part: PartNumber):
        self.part_numbs.append(part)

    def __str__(self):
        return f'{self.symbol}@R{self.position.row} C{self.position.column}'

    def __repr__(self):
        return self.__str__()


def parse_input():

    with open("day3.txt", "r") as fp:
        gamesraw = fp.readlines()

    part_numbers = []
    part_symbols = []

    for rowx, row in enumerate(gamesraw):
        _state = "none"
        _buf = ""
        _start_pos = Coordinate(rowx,0)
        for symbx, symb in enumerate(row):
            if _buf != "" and (symb == "." or symb == '\n' or
                   (_state == "number" and not symb.isdigit())
                   or (_state == "symbol" and symb.isdigit())):
                if _state == "number":
                    pn = PartNumber(int(_buf), _start_pos, Coordinate(rowx, symbx))
                    part_numbers.append(pn)
                if _state == "symbol":
                    ps = PartSymbol(_buf, _start_pos)
                    part_symbols.append(ps)
                _buf = ""
                _state = "none"
            if symb != ".":
                if _buf == "":
                    _start_pos = Coordinate(rowx, symbx)
                    if symb.isdigit():
                        _state = "number"
                    else:
                        _state = "symbol"
                _buf += symb
    return part_numbers, part_symbols


part_numbers, part_symbols = parse_input()

# Check parsing
assert 12 == part_numbers[0].num
assert 935 == part_numbers[1].num
assert 184 == part_numbers[2].num
assert '*' == part_symbols[0].symbol
assert '$' == part_symbols[2].symbol
assert '#' == part_symbols[8].symbol
assert '=' == part_symbols[4].symbol

for part_number in part_numbers:
    for part_symbol in part_symbols:
        if part_symbol.in_range(part_number.row(), part_number.start_col(), part_number.end_col()):
            part_number.symbol = part_symbol
            print(f"Found match: {part_number} = {part_symbol}")
            part_symbol.link_part(part_number)


sum_partnumbers = sum(x.num for x in part_numbers if x.symbol is not None)
num_of_parts_with_no = len([x for x in part_numbers if x.symbol is None])

print(f"Part numbers with no part: {num_of_parts_with_no}")
print(f"Part One: {sum_partnumbers}")

gears = sum([x.part_numbs[0].num * x.part_numbs[1].num for x in part_symbols if x.symbol == '*' and len(x.part_numbs) == 2])

print(f"Sum of gear ratios: {gears}")
