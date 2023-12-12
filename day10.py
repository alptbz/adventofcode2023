import math
from typing import List, Any, Dict


class Node:

    def __init__(self, symbol, x: int, y: int):
        self.symbol = symbol
        self.west: Node = None
        self.east: Node = None
        self.north: Node = None
        self.south: Node = None
        self.x = x
        self.y = y
        self.walked: bool = False

    def __str__(self):
        return f'{self.symbol} ({self.x},{self.y})'

    def __repr__(self):
        return self.__str__()

    def con_south(self):
        return self.symbol in ['|', '7', 'F', 'S']

    def con_north(self):
        return self.symbol in ['|', 'L', 'J', 'S']

    def con_east(self):
        return self.symbol in ['-', 'L', 'F', 'S']

    def con_west(self):
        return self.symbol in ['-', 'J', '7', 'S']

    def unwalked_nodes(self):
        nodes = []
        if self.west is not None and not self.west.walked:
            nodes.append(self.west)
        if self.north is not None and not self.north.walked:
            nodes.append(self.north)
        if self.south is not None and not self.south.walked:
            nodes.append(self.south)
        if self.east is not None and not self.east.walked:
            nodes.append(self.east)
        return nodes


with open('day10.txt') as f:
    lines = f.read().splitlines()

nodes: List[Node] = []
nodes_per_line: Dict[int, List[Node]] = {}

for x, line in enumerate(lines):
    for y, c in enumerate(line):
        if c == ".":
            continue
        n = Node(c, x, y)
        nodes.append(n)
        if x not in nodes_per_line:
            nodes_per_line[x] = []
        nodes_per_line[x].append(n)

nodes_per_line[len(nodes_per_line)] = []
nodes_per_line[-1] = []


for node in nodes:
    other_east_node = next((n for n in nodes_per_line[node.x] if n.x == node.x and n.y == node.y+1), None)
    other_west_node = next((n for n in nodes_per_line[node.x] if n.x == node.x and n.y == node.y-1), None)
    other_north_node = next((n for n in nodes_per_line[node.x-1] if n.x == node.x-1 and n.y == node.y), None)
    other_south_node = next((n for n in nodes_per_line[node.x+1] if n.x == node.x+1 and n.y == node.y), None)
    if other_west_node is not None and other_west_node.con_east() and node.con_west():
        node.west = other_west_node
    if other_south_node is not None and other_south_node.con_north() and node.con_south():
        node.south = other_south_node
    if other_east_node is not None and other_east_node.con_west() and node.con_east():
        node.east = other_east_node
    if other_north_node is not None and other_north_node.con_south() and node.con_north():
        node.north = other_north_node

start_node = next((n for n in nodes if n.symbol == "S"), None)
if start_node.north is not None and start_node.south is not None:
    start_node.symbol = "|"
if start_node.east is not None and start_node.west is not None:
    start_node.symbol = "-"
if start_node.south is not None and start_node.east is not None:
    start_node.symbol = "F"
if start_node.south is not None and start_node.west is not None:
    start_node.symbol = "7"
if start_node.north is not None and start_node.west is not None:
    start_node.symbol = "J"
if start_node.north is not None and start_node.east is not None:
    start_node.symbol = "L"

next_node = start_node

walk_count = 0

while True:
    could_walk = False
    linked_nodes = next_node.unwalked_nodes()
    if len(linked_nodes) == 0:
        break
    next_node.walked = True
    next_node = linked_nodes[0]
    walk_count += 1

next_node.walked = True

print(f'Part One: {math.ceil(walk_count/2)}')

line_length = len(lines[0].strip())

enclosed = 0
inside = False
enter_dir_up = None

for x in range(0, len(lines)):
    line_buf = ""
    for y in range(0, line_length):
        has_node = next((n for n in nodes_per_line[x] if n.x == x and n.y == y and n.walked), None)
        if has_node is None:
            enclosed += inside
            if not inside:
                line_buf += " "
            else:
                line_buf += "I"
        else:
            c = has_node.symbol
            line_buf += c
            if c == "|":
                inside = not inside
            elif c == "L" or c == "F":
                enter_dir_up = c == "L"
            elif c == "J" or c == "7":
                exit_dir_up = c == "J"
                if exit_dir_up != enter_dir_up:
                    inside = not inside

print(f'Part Two: {enclosed}')
