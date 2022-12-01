def prepare_input(file):
    return [line.strip().split() for line in file]


MY_SELECTION = {
    "X": 1,
    "Y": 2,
    "Z": 3
}
RESULT = {
    "X": 0,
    "Y": 3,
    "Z": 6
}


def rock_paper_scissors_p1(s1, s2):
    if s1 == "A" and s2 == "X":
        return 3
    elif s1 == "A" and s2 == "Y":
        return 6
    elif s1 == "A" and s2 == "Z":
        return 0
    if s1 == "B" and s2 == "X":
        return 0
    elif s1 == "B" and s2 == "Y":
        return 3
    elif s1 == "B" and s2 == "Z":
        return 6
    if s1 == "C" and s2 == "X":
        return 6
    elif s1 == "C" and s2 == "Y":
        return 0
    elif s1 == "C" and s2 == "Z":
        return 3


def part_one(_input):
    global MY_SELECTION
    _sum = 0

    for s1, s2 in _input:
        _sum += MY_SELECTION[str(s2)]
        _sum += rock_paper_scissors_p1(str(s1), str(s2))

    return _sum


def rock_paper_scissors_p2(s1, s2):
    if s1 == "A" and s2 == "X":
        return 3
    elif s1 == "A" and s2 == "Y":
        return 1
    elif s1 == "A" and s2 == "Z":
        return 2
    if s1 == "B" and s2 == "X":
        return 1
    elif s1 == "B" and s2 == "Y":
        return 2
    elif s1 == "B" and s2 == "Z":
        return 3
    if s1 == "C" and s2 == "X":
        return 2
    elif s1 == "C" and s2 == "Y":
        return 3
    elif s1 == "C" and s2 == "Z":
        return 1


def part_two(_input):
    global RESULT
    _sum = 0

    for s1, s2 in _input:
        _sum += rock_paper_scissors_p2(str(s1), str(s2))
        _sum += RESULT[str(s2)]

    return _sum


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
