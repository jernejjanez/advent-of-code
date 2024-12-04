import re


def prepare_input(file):
    return [re.findall("mul\((\d{1,3}),(\d{1,3})\)", line) for line in file]


def part_one(_input):
    _sum = 0

    for line in _input:
        for _tuple in line:
            v1, v2 = _tuple
            _sum += int(v1) * int(v2)

    return _sum


def prepare_input_part2(file):
    data = ""
    for line in file:
        data += line.strip()

    data = re.sub("don't\(\).+?(do\(\)|$)", "", data)
    return [re.findall("mul\((\d{1,3}),(\d{1,3})\)", data)]


def part_two(_input):
    return part_one(_input)


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        _input = prepare_input(f)

    answer1 = part_one(_input)
    print("Part one:")
    print("Answer: {}".format(answer1))
    print()

    with open('input.txt', 'r') as f:
        _input = prepare_input_part2(f)

    answer2 = part_two(_input)
    print("Part two:")
    print("Answer: {}".format(answer2))
