def prepare_input(file):
    return [None if str(line) == '\n' else int(line) for line in file]


def part_one(_input):
    _max = 0
    current = 0

    for line in _input:
        if line is not None:
            current += line
        else:
            if current > _max:
                _max = current
            current = 0

    return _max


def part_two(_input):
    max_1 = 0
    max_2 = 0
    max_3 = 0
    current = 0

    for line in _input:
        if line is not None:
            current += line
        else:
            if current > max_1:
                max_1 = current
            elif current > max_2:
                max_2 = current
            elif current > max_3:
                max_3 = current
            current = 0

    return max_1 + max_2 + max_3


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        _input = prepare_input(f)

    answer1 = part_one(_input)
    print("Part one:")
    print("Answer: {}".format(int(answer1)))
    print()
    answer2 = part_two(_input)
    print("Part two:")
    print("Answer: {}".format(int(answer2)))
