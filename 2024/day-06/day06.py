import copy
import numpy as np


ROWS = 0
COLUMNS = 0


def prepare_input(file):
    return [line.strip() for line in file]


def prepare_map(_map):
    global ROWS, COLUMNS
    ROWS = len(_map)
    COLUMNS = len(_map[0])
    _map_array = np.zeros((ROWS, COLUMNS), str)
    for i, row in enumerate(_map):
        _map_array[i] = np.array([c for c in row])

    return _map_array


def find_node(_map, char):
    for y, y_row in enumerate(_map):
        for x, _ in enumerate(y_row):
            if _map[y][x] == char:
                return y, x


def move_node(i, j, move):
    return i + move[0], j + move[1]


def undo_move(i, j, move):
    return i - move[0], j - move[1]


def is_on_map(i, j):
    global ROWS, COLUMNS
    if 0 <= i < ROWS and 0 <= j < COLUMNS:
        return True
    return False


def part_one(_input):
    visited_locations = []
    _map_array = prepare_map(_input)
    y, x = find_node(_map_array, "^")
    visited_locations.append((x, y))
    directions = [[0, -1], [1, 0], [0, 1], [-1, 0]] # up, right, down, left
    move = directions.pop(0)
    while is_on_map(x, y):
        if _map_array[y][x] == "#":
            x, y = undo_move(x, y, move)
            directions.append(move)
            move = directions.pop(0)

        x, y = move_node(x, y, move)

        if (x, y) not in visited_locations and is_on_map(x, y) and _map_array[y][x] != "#":
            visited_locations.append((x, y))

    return len(visited_locations)


def is_loop(_input):
    visited_locations = []
    _map_array = prepare_map(_input)
    start_y, start_x = find_node(_map_array, "^")
    y, x = start_y, start_x
    visited_locations.append((x, y))
    directions = [[0, -1], [1, 0], [0, 1], [-1, 0]]  # up, right, down, left
    move = directions.pop(0)
    count = 0
    _max = 10000
    while is_on_map(x, y) and count <= _max:
        if _map_array[y][x] == "#":
            x, y = undo_move(x, y, move)
            directions.append(move)
            move = directions.pop(0)

        x, y = move_node(x, y, move)
        count += 1

        if (x, y) not in visited_locations and is_on_map(x, y) and _map_array[y][x] != "#":
            visited_locations.append((x, y))

    if count > _max:
        return True
    return False


def part_two(_input):
    visited_locations = []
    _map_array = prepare_map(_input)
    y, x = find_node(_map_array, "^")
    visited_locations.append((x, y))
    directions = [[0, -1], [1, 0], [0, 1], [-1, 0]]  # up, right, down, left
    move = directions.pop(0)
    while is_on_map(x, y):
        if _map_array[y][x] == "#":
            x, y = undo_move(x, y, move)
            directions.append(move)
            move = directions.pop(0)

        x, y = move_node(x, y, move)

        if (x, y) not in visited_locations and is_on_map(x, y) and _map_array[y][x] != "#":
            visited_locations.append((x, y))

    visited_locations = visited_locations[1:]
    count = 0
    for x, y in visited_locations:
        modified_map = _map_array.copy()
        modified_map[y][x] = "#"
        if is_loop(modified_map):
            count += 1

    return count


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
