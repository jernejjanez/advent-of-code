PRIORITIES = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
    "A": 27,
    "B": 28,
    "C": 29,
    "D": 30,
    "E": 31,
    "F": 32,
    "G": 33,
    "H": 34,
    "I": 35,
    "J": 36,
    "K": 37,
    "L": 38,
    "M": 39,
    "N": 40,
    "O": 41,
    "P": 42,
    "Q": 43,
    "R": 44,
    "S": 45,
    "T": 46,
    "U": 47,
    "V": 48,
    "W": 49,
    "X": 50,
    "Y": 51,
    "Z": 52
}


def prepare_input(file):
    return [line.strip() for line in file]


def get_priorities_p1(p1, p2):
    global PRIORITIES
    for c in p1:
        if c in p2:
            return PRIORITIES[c]


def part_one(_input):
    _sum = 0

    for s in _input:
        p1 = s[0:int(len(s)/2)]
        p2 = s[int(len(s)/2):len(s)]

        _sum += get_priorities_p1(p1, p2)

    return _sum


def get_priorities_p2(s1, s2, s3):
    global PRIORITIES
    for c in s1:
        if c in s2 and c in s3:
            return PRIORITIES[c]


def part_two(_input):
    _sum = 0
    group = 3
    i = 1
    p = {
        1: "",
        2: "",
        3: ""
    }
    for s in _input:
        p[i] = s
        i += 1
        if i > group:
            _sum += get_priorities_p2(p[1], p[2], p[3])
            i = 1

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
