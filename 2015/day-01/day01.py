import copy


def prepare_input(file):
    for line in file:
        return line.strip()


def part_one(_input):
    floor = 0
    for instruction in _input:
        if instruction == "(":
            floor += 1
        elif instruction == ")":
            floor -= 1
    return floor


def part_two(_input):
    floor = 0
    for i, instruction in enumerate(_input):
        if instruction == "(":
            floor += 1
        elif instruction == ")":
            floor -= 1
        if floor == -1:
            return i + 1


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
