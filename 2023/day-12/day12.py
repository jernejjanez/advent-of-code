import copy
import re


def prepare_input(file):
    springs_list = []
    contiguous_groups = []
    for line in file:
        springs, groups = line.strip().split()
        springs_list.append(springs)
        contiguous_groups.append(list(map(int, groups.split(","))))
    return springs_list, contiguous_groups


# def get_contiguous_group(size):
#     return "." + size * "#" + "."

def get_contiguous_group(size):
    return size * "#"


def is_spring_possible_at(springs, possible_springs, start, end):
    # TODO: ? and # can be combined
    reg = "(?:#|\?){" + str(len(possible_springs)) + "}"
    return springs[start:end] == possible_springs or re.compile(reg).match(springs[start:end])


def find_all_possible_arrangements(springs, groups):
    are_any_arrangements_left = True
    while are_any_arrangements_left:
        used_springs = 0
        positions = {}
        for group in groups:
            possible_springs = get_contiguous_group(group)
            for i in range(used_springs, len(springs)):
                if is_spring_possible_at(springs, possible_springs, i, i + len(possible_springs)):
                    if i == 0 and springs[i + len(possible_springs)] != "#" or i == len(springs) - len(possible_springs) and springs[i - len(possible_springs)] != "#":
                        used_springs += len(possible_springs) + 1
                        positions[i] = len(possible_springs)
                        break
                    if springs[i + len(possible_springs)] != "#" and springs[i - len(possible_springs)] != "#":
                        used_springs += len(possible_springs) + 1
                        positions[i] = len(possible_springs)
                        break

    return 1


def part_one(_input):
    springs_list, contiguous_groups = _input
    _sum = 0
    for springs, groups in zip(springs_list, contiguous_groups):
        _sum += find_all_possible_arrangements(springs, groups)
    return _sum


def part_two(_input):
    return 0


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
