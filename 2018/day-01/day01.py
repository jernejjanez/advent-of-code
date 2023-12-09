import copy


def prepare_input(file):
    return [(line[0], int(line.strip()[1:])) for line in file]


def part_one(_input):
    frequency = 0
    for operator, change in _input:
        if operator == "+":
            frequency += change
        if operator == "-":
            frequency -= change
    return frequency


def part_two(_input):
    frequency = 0
    seen_frequency = []
    while True:
        for operator, change in _input:
            if operator == "+":
                frequency += change
            if operator == "-":
                frequency -= change
            if frequency in seen_frequency:
                return frequency
            seen_frequency.append(frequency)


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
