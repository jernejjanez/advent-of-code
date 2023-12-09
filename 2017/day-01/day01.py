import copy


def prepare_input(file):
    for line in file:
        return line.strip()


def part_one(_input):
    _sum = 0
    for i in range(len(_input)):
        if i == len(_input) - 1:
            if _input[i] == _input[0]:
                _sum += int(_input[i])
        elif _input[i] == _input[i + 1]:
            _sum += int(_input[i])
    return _sum


def part_two(_input):
    _sum = 0
    items_ahead = int(len(_input) / 2)
    for i in range(len(_input)):
        if i + items_ahead > len(_input) - 1:
            if _input[i] == _input[(i + items_ahead) - len(_input)]:
                _sum += int(_input[i])
        elif _input[i] == _input[i + items_ahead]:
            _sum += int(_input[i])
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
