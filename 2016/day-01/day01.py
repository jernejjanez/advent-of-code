import copy


def prepare_input(file):
    for line in file:
        return line.strip().split(", ")


def move(horizontal_position, vertical_position, direction, blocks):
    if direction == "N":
        vertical_position += blocks
    elif direction == "E":
        horizontal_position += blocks
    elif direction == "S":
        vertical_position -= blocks
    elif direction == "W":
        horizontal_position -= blocks
    return horizontal_position, vertical_position


def part_one(_input):
    directions = "NESW"
    current_direction = "N"
    horizontal_position = 0
    vertical_position = 0
    for instruction in _input:
        turn = instruction[0]
        blocks = int(instruction[1:])
        if turn == "R":
            if directions.index(current_direction) + 1 == len(directions):
                current_direction = directions[0]
            else:
                current_direction = directions[directions.index(current_direction) + 1]
        elif turn == "L":
            current_direction = directions[directions.index(current_direction) - 1]
        horizontal_position, vertical_position = move(horizontal_position, vertical_position, current_direction, blocks)
    return abs(horizontal_position) + abs(vertical_position)


def move_one_step(horizontal_position, vertical_position, direction):
    if direction == "N":
        vertical_position += 1
    elif direction == "E":
        horizontal_position += 1
    elif direction == "S":
        vertical_position -= 1
    elif direction == "W":
        horizontal_position -= 1
    return horizontal_position, vertical_position


def part_two(_input):
    directions = "NESW"
    current_direction = "N"
    horizontal_position = 0
    vertical_position = 0
    visited = []
    for instruction in _input:
        turn = instruction[0]
        blocks = int(instruction[1:])
        if turn == "R":
            if directions.index(current_direction) + 1 == len(directions):
                current_direction = directions[0]
            else:
                current_direction = directions[directions.index(current_direction) + 1]
        elif turn == "L":
            current_direction = directions[directions.index(current_direction) - 1]
        for _ in range(blocks):
            horizontal_position, vertical_position = move_one_step(horizontal_position, vertical_position, current_direction)
            if (horizontal_position, vertical_position) in visited:
                return abs(horizontal_position) + abs(vertical_position)
            else:
                visited.append((horizontal_position, vertical_position))


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
