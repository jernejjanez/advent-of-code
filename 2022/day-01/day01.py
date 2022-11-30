def part_one(_input=[]):
    print("Part one result")


def part_two(_input=[]):
    print("Part two result")


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        lines = [int(line) for line in file]

    print("Part one:")
    part_one(lines)
    print()
    print("Part two:")
    part_two(lines)
