import copy


def prepare_input(file):
    return [list(map(int, line.strip().split())) for line in file]


def check_if_safe(line):
    increasing = False
    decreasing = False
    for i, v in enumerate(line):
        if i + 1 == len(line):
            return True
        if i == 0:
            if v > line[i + 1]:
                decreasing = True
            elif v < line[i + 1]:
                increasing = True
            else:
                return False
        if increasing and v >= line[i + 1]:
            return False
        if decreasing and v <= line[i + 1]:
            return False
        if abs(v - line[i + 1]) > 3:
            return False


def part_one(_input):
    _sum = 0

    for line in _input:
        if check_if_safe(line):
            _sum += 1

    return _sum


def part_two(_input):
    _sum = 0

    for line in _input:
        if check_if_safe(line):
            _sum += 1
            continue
        for i, _ in enumerate(line):
            line1 = copy.deepcopy(line)
            del line1[i]
            if check_if_safe(line1):
                _sum += 1
                break


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
