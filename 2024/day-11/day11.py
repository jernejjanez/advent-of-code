import copy
from functools import cache

def prepare_input(file):
    return [line.strip().split() for line in file][0]

def part_one(_input):
    for _ in range(25):
        idx = 0
        while idx < len(_input):
            number = _input[idx]
            if number == "0":
                _input[idx] = "1"
            elif len(number) % 2 == 0:
                split_idx = len(number) // 2
                _input[idx] = str(int(number[split_idx:]))
                _input.insert(idx, number[:split_idx])
                idx += 1
            else:
                _input[idx] = str(int(number) * 2024)
            idx += 1
    return len(_input)

@cache
def count_stones(number, depth):
    if depth == 0:
        return 1
    if number == "0":
        return count_stones("1", depth-1)
    if len(number) % 2 == 0:
        split_idx = len(number) // 2
        return count_stones(number[:split_idx], depth-1) + count_stones(str(int(number[split_idx:])), depth-1)
    return count_stones(str(int(number) * 2024), depth-1)

def part_two(_input):
    _sum = 0
    for number in _input:
        _sum += count_stones(number, 75)
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
