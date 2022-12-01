def prepare_input(file):
    return [int(line) for line in file]


def part_one(_input):
    goal = 2020

    for number1 in _input:
        for number2 in _input:
            if number1 + number2 == goal:
                return number1 * number2

    return -1


def part_two(_input):
    goal = 2020

    for number1 in _input:
        for number2 in _input:
            for number3 in _input:
                if number1 + number2 + number3 == goal:
                    return number1 * number2 * number3

    return -1


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
