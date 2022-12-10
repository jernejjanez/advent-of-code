import copy


def string_to_int(string_or_int):
    try:
        return int(string_or_int)
    except ValueError:
        return string_or_int


def prepare_input(file):
    return [list(map(string_to_int, list(line.split()))) for line in file]


def helper_p1(cycle):
    if cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220:
        return True
    return False


def part_one(_input):
    result = []
    x = 1
    cycle = 1
    for inst in _input:
        if inst[0] == "noop":
            if helper_p1(cycle):
                result.append(cycle * x)
            cycle += 1
            continue
        else:
            _, v = inst
            for j in range(2):
                if helper_p1(cycle):
                    result.append(cycle * x)
                if j != 0:
                    x += v
                cycle += 1

    return sum(result)


def helper_p2(cycle):
    if cycle == 40 or cycle == 80 or cycle == 120 or cycle == 160 or cycle == 200 or cycle == 240:
        return True
    return False


def part_two(_input):
    x = 1
    cycle = 1
    curr_pos = 0
    for inst in _input:
        if inst[0] == "noop":
            print("#", end="") if curr_pos in [x, x - 1, x + 1] else print(".", end="")
            curr_pos += 1
            if helper_p2(cycle):
                curr_pos = 0
                print()
            cycle += 1
            continue
        else:
            _, v = inst
            for j in range(2):
                print("#", end="") if curr_pos in [x, x - 1, x + 1] else print(".", end="")
                curr_pos += 1
                if helper_p2(cycle):
                    curr_pos = 0
                    print()
                if j != 0:
                    x += v
                cycle += 1


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        _input = prepare_input(f)

    _input_copy = copy.deepcopy(_input)
    answer1 = part_one(_input_copy)
    print("Part one:")
    print("Answer: {}".format(answer1))
    print()
    print("Part two:")
    part_two(_input)
    # print("Answer: {}".format(answer2))
