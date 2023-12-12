import math
from typing import Self, List, Any
import re

class Node:

    def __init__(self, id: str):
        self.id = id
        self.left: Node = None
        self.right: Node = None

    def set_left(self, left: Self):
        self.left = left

    def set_right(self, right: Self):
        self.right = right

    def __str__(self):
        return self.id

    def __repr__(self):
        return self.__str__()


with open("day8.txt", "r") as fp:
    lines_raw = fp.readlines()

walk_instructions = lines_raw[0].strip()

nodes = []

for node_in in lines_raw[2:]:
    node_in = node_in.strip()
    parts = list(re.findall(r'\w+', node_in))
    nodes.append(Node(parts[0]))

for node_in in lines_raw[2:]:
    node_in = node_in.strip()
    parts = list(re.findall(r'\w+', node_in))
    node = [n for n in nodes if n.id == parts[0]][0]
    node_left = [n for n in nodes if n.id == parts[1]][0]
    node_right = [n for n in nodes if n.id == parts[2]][0]
    node.set_left(node_left)
    node.set_right(node_right)

current_node = [n for n in nodes if n.id == "AAA"][0]

steps = 0

for t in range(0, 100000):
    for walk in walk_instructions:
        if walk == 'L':
            current_node = current_node.left
        else:
            current_node = current_node.right
        steps += 1
        if current_node.id == "ZZZ":
            break
    if current_node.id == "ZZZ":
        break


print(current_node.id)
print(f"Part One: {steps}")

nodes_ending_with_a = [n for n in nodes if n.id.endswith('A')]
nodes_ending_with_z = [n for n in nodes if n.id.endswith('Z')]
num_of_steps: List[Any] = [None] * len(nodes_ending_with_a)
total_a_nodes = len(nodes_ending_with_a)
steps = 0

for t in range(0, 100000):
    nodes_with_z_count = 0
    for walk in walk_instructions:
        if walk == 'L':
            for i in range(0, len(nodes_ending_with_a)):
                if num_of_steps[i] is None:
                    nodes_ending_with_a[i] = nodes_ending_with_a[i].left
        else:
            for i in range(0, len(nodes_ending_with_a)):
                if num_of_steps[i] is None:
                    nodes_ending_with_a[i] = nodes_ending_with_a[i].right
        steps += 1
        for i in range(0, len(nodes_ending_with_a)):
            if nodes_ending_with_a[i].id.endswith("Z") and num_of_steps[i] is None:
                num_of_steps[i] = steps
        if None not in num_of_steps:
            break
    if None not in num_of_steps:
        break


total_steps_part_b = math.lcm(*num_of_steps)

print(f"Part Two: {total_steps_part_b}")
