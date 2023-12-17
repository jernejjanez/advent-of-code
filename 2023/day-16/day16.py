import copy

import numpy as np

ROWS = 0
COLUMNS = 0


def prepare_input(file):
    values = []
    for line in file:
        values.append([*line.strip()])
    return values


def prepare_numpy_map(_input):
    global ROWS, COLUMNS
    ROWS = len(_input)
    COLUMNS = len(_input[0])
    numpy_map = np.zeros((ROWS, COLUMNS), str)
    for i, row in enumerate(_input):
        numpy_map[i] = np.array(row)
    return numpy_map


def get_next_location(y, x, direction):
    if direction == "right":
        return y, x + 1, direction
    if direction == "left":
        return y, x - 1, direction
    if direction == "up":
        return y - 1, x, direction
    if direction == "down":
        return y + 1, x, direction


def check_if_visited_with_direction(tiles, y, x, direction):
    return (y, x) in tiles and direction in tiles[(y, x)]


def move(_map, y, x, direction, tiles):
    while 0 <= x < ROWS and 0 <= y < COLUMNS:
        if check_if_visited_with_direction(tiles, y, x, direction):
            return tiles
        else:
            if (y, x) in tiles:
                tiles[(y, x)].append(direction)
            else:
                tiles[(y, x)] = [direction]

        if _map[y][x] == ".":
            y, x, direction = get_next_location(y, x, direction)
        elif _map[y][x] == "|":
            if direction == "up" or direction == "down":
                y, x, direction = get_next_location(y, x, direction)
            elif direction == "right" or direction == "left":
                y1, x1, direction = get_next_location(y, x, "up")
                tiles = move(_map, y1, x1, "up", tiles)
                y, x, direction = get_next_location(y, x, "down")
        elif _map[y][x] == "-":
            if direction == "up" or direction == "down":
                y1, x1, direction = get_next_location(y, x, "left")
                tiles = move(_map, y1, x1, "left", tiles)
                y, x, direction = get_next_location(y, x, "right")
            elif direction == "right" or direction == "left":
                y, x, direction = get_next_location(y, x, direction)
        elif _map[y][x] == "/":
            if direction == "up":
                y, x, direction = get_next_location(y, x, "right")
            elif direction == "down":
                y, x, direction = get_next_location(y, x, "left")
            elif direction == "left":
                y, x, direction = get_next_location(y, x, "down")
            elif direction == "right":
                y, x, direction = get_next_location(y, x, "up")
        elif _map[y][x] == "\\":
            if direction == "up":
                y, x, direction = get_next_location(y, x, "left")
            elif direction == "down":
                y, x, direction = get_next_location(y, x, "right")
            elif direction == "left":
                y, x, direction = get_next_location(y, x, "up")
            elif direction == "right":
                y, x, direction = get_next_location(y, x, "down")
    return tiles


def part_one(_input):
    numpy_map = prepare_numpy_map(_input)
    tiles = move(numpy_map, 0, 0, "right", {})
    return len(tiles)


def part_two(_input):
    numpy_map = prepare_numpy_map(_input)
    tiles_array = {}
    for x in range(ROWS):
        tiles_array[(0, x, "down")] = move(numpy_map, 0, x, "down", {})
        tiles_array[(COLUMNS - 1, x, "up")] = move(numpy_map, COLUMNS - 1, x, "up", {})
    for y in range(COLUMNS):
        tiles_array[(y, 0, "right")] = move(numpy_map, y, 0, "right", {})
        tiles_array[(y, ROWS - 1, "left")] = move(numpy_map, y, ROWS - 1, "left", {})

    max_tiles = 0
    for _, tiles in tiles_array.items():
        if len(tiles) > max_tiles:
            max_tiles = len(tiles)
    return max_tiles


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
