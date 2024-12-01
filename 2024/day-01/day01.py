import copy


def prepare_input(file):
    l1 = []
    l2 = []
    for line in file:
        v1, v2 = line.strip().split()
        l1.append(v1)
        l2.append(v2)
    return list(map(int, l1)), list(map(int, l2))


def part_one(_input):
    _sum = 0

    l1, l2 = _input
    l1.sort()
    l2.sort()

    for v1, v2 in zip(l1, l2):
        _sum += abs(v1 - v2)

    return _sum


def part_two(_input):
    _sum = 0

    calculated_values = {}
    l1, l2 = _input

    for v1 in l1:
        if v1 not in calculated_values:
            occurrences = l2.count(v1)
            if occurrences > 0:
                _sum += occurrences * v1
            calculated_values[v1] = occurrences * v1
        else:
            _sum += calculated_values[v1]

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
