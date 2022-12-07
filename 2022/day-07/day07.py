import copy
import random


def prepare_input(file):
    _dict = {}
    curr_dir = ("/", None)
    active_dirs = ["/"]
    for line in file:
        if line[0] == "$":
            command = line[2:].split()[0]
            if command == "cd":
                arg = line[2:].split()[1]
                if arg == "..":
                    curr_dir = curr_dir[1]
                    active_dirs.pop()
                elif arg == "/":
                    curr_dir = ("/", None)
                    active_dirs = ["/"]
                else:
                    # Different folders can have the same name => add a random number to make them distinct
                    dir_name = arg + str(random.randint(1, 100000))
                    curr_dir = (dir_name, curr_dir)
                    active_dirs.append(dir_name)
        else:
            size, _ = line.split()
            if size != "dir":
                for d in active_dirs:
                    if d not in _dict:
                        _dict[d] = int(size)
                    else:
                        _dict[d] += int(size)

    return _dict


def part_one(_input):
    result = 0
    for v in _input.values():
        if v <= 100000:
            result += v

    return result


def part_two(_input):
    disk_space = 70000000
    needed_space = 30000000
    available_space = disk_space - _input["/"]

    sorted_input = dict(sorted(_input.items(), key=lambda x: x[1]))
    for v in sorted_input.values():
        if available_space + v >= needed_space:
            return v

    return -1


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
