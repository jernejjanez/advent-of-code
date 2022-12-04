def prepare_input(file):
    return [line.strip().split(",") for line in file]


def part_one(_input):
    _count = 0

    for a1, a2 in _input:
        a1_l, a1_h = map(int, a1.split("-"))
        a2_l, a2_h = map(int, a2.split("-"))

        if a1_l >= a2_l and a1_h <= a2_h or a2_l >= a1_l and a2_h <= a1_h:
            _count += 1

    return _count


def _fun_p2(l1, h1, l2, h2):
    for i in range(l1, h1+1):
        if l2 <= i <= h2:
            return 1
    return 0


def part_two(_input):
    _count = 0

    for a1, a2 in _input:
        a1_l, a1_h = map(int, a1.split("-"))
        a2_l, a2_h = map(int, a2.split("-"))

        _count += _fun_p2(a1_l, a1_h, a2_l, a2_h)

    return _count


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
