import copy


def prepare_input(file):
    platform = []
    for line in file:
        line = line.strip()
        platform.append(line)
    return platform


def move_rocks_and_calculate_load(line):
    _sum = 0
    load = len(line)
    current_available_position = 0
    for i in range(len(line)):
        if line[i] == "O":
            _sum += load - current_available_position
            current_available_position += 1
        elif line[i] == "#":
            current_available_position = i + 1
    return _sum


def part_one(_input):
    platform = [(''.join(list(i)[0::])) for i in zip(*_input)]
    _sum = 0
    for line in platform:
        _sum += move_rocks_and_calculate_load(line)
    return _sum


def move_rocks(line):
    current_available_position = 0
    for i in range(len(line)):
        if line[i] == "O":
            if i != current_available_position:
                line = line[:i] + "." + line[i + 1:]
                line = line[:current_available_position] + "O" + line[current_available_position + 1:]
            current_available_position += 1
        elif line[i] == "#":
            current_available_position = i + 1
    return line


def cycle(platform):
    for direction in ["north", "west", "south", "east"]:
        if direction == "north":
            platform = [(''.join(list(i)[0::])) for i in zip(*platform)]
        elif direction == "west":
            platform = [(''.join(list(i)[0::])) for i in zip(*platform)]
        elif direction == "south":
            platform = [(''.join(list(i)[::-1])) for i in zip(*platform)]
        elif direction == "east":
            platform = [(''.join(list(i)[::-1])) for i in zip(*platform)]
        for i in range(len(platform)):
            platform[i] = move_rocks(platform[i])
    platform = [(''.join(list(i)[::-1])) for i in zip(*platform)]
    platform = [(''.join(list(i)[::-1])) for i in zip(*platform)]
    return platform


def calculate_load(platform):
    _sum = 0
    load = len(platform)
    for i, line in enumerate(platform):
        _sum += (load - i) * line.count("O")
    return _sum


def find_repetition(loads):
    repetition = []
    index = 0
    for x in range(len(loads)):
        for y in range(x + 1, len(loads)):
            if loads[x:y] == loads[y:2 * y] and len(loads[x:y]) != 1:
                repetition = loads[x:y]
                index = x
    return repetition, index


def find_correct_load(repetition, position):
    return repetition[(999999999 - position) % len(repetition)]


def part_two(_input):
    platform = _input
    loads = []
    for i in range(500):
        platform = cycle(platform)
        loads.append(calculate_load(platform))
    repetition, position = find_repetition(loads)
    return find_correct_load(repetition, position)


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
