import copy
import math


def prepare_input(file):
    nodes = {}
    instructions = ""
    for i, line in enumerate(file):
        line = line.strip()
        if i == 0:
            instructions = line
        elif i == 1:
            continue
        else:
            node, left_right = line.split(" = ")
            left, right = left_right.split(", ")
            left = left[1:]
            right = right[:-1]
            nodes[node] = (left, right)
    return nodes, instructions


def part_one(_input):
    nodes, instructions = _input
    current_node = "AAA"
    steps = 0
    while current_node != "ZZZ":
        for instruction in instructions:
            if instruction == "L":
                current_node = nodes[current_node][0]
            if instruction == "R":
                current_node = nodes[current_node][1]
            steps += 1
    return steps


def is_end_node(node):
    return node.rfind("Z") == 2


def part_two(_input):
    nodes, instructions = _input
    all_starting_nodes = []
    for key, _ in nodes.items():
        if key.rfind("A") == 2:
            all_starting_nodes.append(key)
    steps_list = []
    for i in range(len(all_starting_nodes)):
        steps = 0
        while not is_end_node(all_starting_nodes[i]):
            for instruction in instructions:
                if instruction == "L":
                    all_starting_nodes[i] = nodes[all_starting_nodes[i]][0]
                if instruction == "R":
                    all_starting_nodes[i] = nodes[all_starting_nodes[i]][1]
                steps += 1
        steps_list.append(steps)
    return math.lcm(*steps_list)


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        _input = prepare_input(f)

    _input_copy = copy.deepcopy(_input)
    answer1 = part_one(_input_copy)
    print("Part one:")
    print("Answer: {}".format(answer1))
    print()
    answer2 = part_two(_input)
    print("Part two:")
    print("Answer: {}".format(answer2))
