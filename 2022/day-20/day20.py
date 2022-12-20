def prepare_input(file):
    input_part1 = []
    input_part2 = []
    for idx, line in enumerate(file):
        input_part1.append((idx, int(line.strip())))
        input_part2.append((idx, int(line.strip()) * 811589153))

    return input_part1, input_part2

def part_one(_input):
    idx_1 = 0
    while idx_1 != len(_input):
        for _input_idx, item in enumerate(_input):
            idx_2, value = item
            if idx_1 == idx_2:
                _input.pop(_input_idx)
                _input.insert((_input_idx + value) % len(_input), (idx_2, value))
                break
        idx_1 += 1

    while _input[0][1] != 0:
        _input.append(_input.pop(0))

    result = 0
    result += _input[1000 % len(_input)][1]
    result += _input[2000 % len(_input)][1]
    result += _input[3000 % len(_input)][1]

    return result

def part_two(_input):
    for _ in range(10):
        idx_1 = 0
        while idx_1 != len(_input):
            for _input_idx, item in enumerate(_input):
                idx_2, value = item
                if idx_1 == idx_2:
                    _input.pop(_input_idx)
                    _input.insert((_input_idx + value) % len(_input), (idx_2, value))
                    break
            idx_1 += 1

    while _input[0][1] != 0:
        _input.append(_input.pop(0))

    result = 0
    result += _input[1000 % len(_input)][1]
    result += _input[2000 % len(_input)][1]
    result += _input[3000 % len(_input)][1]

    return result

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        _input, _input_2 = prepare_input(f)

    answer1 = part_one(_input)
    print("Part one:")
    print("Answer: {}".format(answer1))
    print()
    answer2 = part_two(_input_2)
    print("Part two:")
    print("Answer: {}".format(answer2))
