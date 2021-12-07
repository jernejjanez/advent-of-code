def unit_to_int(command):
    try:
        return int(command)
    except ValueError:
        return command


def part_one(commands):
    horizontal_position = 0
    depth = 0
    for (command, units) in commands:
        if command == "forward":
            horizontal_position += units
        elif command == "down":
            depth += units
        elif command == "up":
            depth -= units

    print("Part one:")
    print("Horizontal position: {}".format(horizontal_position))
    print("Depth: {}".format(depth))
    print("Answer: {}".format(horizontal_position * depth))


def part_two(commands):
    horizontal_position = 0
    depth = 0
    aim = 0
    for (command, units) in commands:
        if command == "forward":
            horizontal_position += units
            depth += aim * units
        elif command == "down":
            aim += units
        elif command == "up":
            aim -= units

    print("Part two:")
    print("Horizontal position: {}".format(horizontal_position))
    print("Depth: {}".format(depth))
    print("Aim: {}".format(aim))
    print("Answer: {}".format(horizontal_position * depth))


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        planned_course = [tuple(map(unit_to_int, line.split())) for line in f]

part_one(planned_course)
print()
part_two(planned_course)
