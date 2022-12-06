import copy
from collections import Counter


def prepare_input(file):
    for line in file:
        return line.strip()


def part_one(_input):
    idx = 0

    for _ in _input:
        freq = Counter(_input[idx:idx + 4])
        if len(freq) == 4:
            return idx + 4
        idx += 1

    return -1


def part_two(_input):
    idx = 0

    for _ in _input:
        freq = Counter(_input[idx:idx + 14])
        if len(freq) == 14:
            return idx + 14
        idx += 1

    return -1


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
