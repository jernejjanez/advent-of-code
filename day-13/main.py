import copy
import itertools


def string_to_int(string_or_int):
    try:
        return int(string_or_int)
    except ValueError:
        return string_or_int


def prepare_input(file):
    lines_are_instructions = False
    coordinates = []
    instructions = []
    for line in file:
        if line == "\n":
            lines_are_instructions = True
            continue
        elif lines_are_instructions:
            instructions.append(list(map(string_to_int, line.strip().split()[2].split("="))))
        else:
            coordinates.append(list(map(int, line.strip().split(","))))

    return instructions, coordinates


def part_one(_input):
    instructions, coordinates = copy.deepcopy(_input)
    first_instruction = instructions[0]
    direction, position = first_instruction

    visible_dots = []
    if direction == "x":
        for coordinate in coordinates:
            if coordinate[0] > position:
                visible_dots.append([coordinate[0] - (2 * (coordinate[0] - position)), coordinate[1]])
            else:
                visible_dots.append(coordinate)
    elif direction == "y":
        for coordinate in coordinates:
            if coordinate[1] > position:
                visible_dots.append([coordinate[0], coordinate[1] - (2 * (coordinate[1] - position))])
            else:
                visible_dots.append(coordinate)

    visible_dots.sort()
    visible_dots = list(k for k, _ in itertools.groupby(visible_dots))

    return len(visible_dots)


def part_two(_input):
    instructions, coordinates = copy.deepcopy(_input)

    for direction, position in instructions:
        visible_dots = []
        if direction == "x":
            for coordinate in coordinates:
                if coordinate[0] > position:
                    visible_dots.append([coordinate[0] - (2 * (coordinate[0] - position)), coordinate[1]])
                else:
                    visible_dots.append(coordinate)
        elif direction == "y":
            for coordinate in coordinates:
                if coordinate[1] > position:
                    visible_dots.append([coordinate[0], coordinate[1] - (2 * (coordinate[1] - position))])
                else:
                    visible_dots.append(coordinate)

        coordinates = copy.deepcopy(visible_dots)

    coordinates.sort()
    coordinates = list(k for k, _ in itertools.groupby(coordinates))
    max_x = max([sublist[1] for sublist in coordinates])
    max_y = max([sublist[0] for sublist in coordinates])
    for x in range(max_x + 1):
        for y in range(max_y + 1):
            if [y, x] in coordinates:
                print("#", end=" ")
            else:
                print(".", end=" ")
        print()
    print()


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        _input = prepare_input(f)

    answer1 = part_one(_input)
    print("Part one:")
    print("Answer: {}".format(int(answer1)))
    print()
    print("Part two:")
    part_two(_input)
