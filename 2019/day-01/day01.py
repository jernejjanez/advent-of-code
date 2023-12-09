import copy
import math


def prepare_input(file):
    return [int(line.strip()) for line in file]


def part_one(_input):
    _sum = 0
    for mass in _input:
        _sum += math.floor(mass / 3) - 2
    return _sum


def part_two(_input):
    _sum = 0
    for mass in _input:
        while math.floor(mass / 3) - 2 > 0:
            mass = math.floor(mass / 3) - 2
            _sum += mass
    return _sum


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
