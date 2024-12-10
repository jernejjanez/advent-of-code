import copy
import numpy as np

COUNT = 0
ROWS = 0
COLUMNS = 0

def prepare_input(file):
    return [line.strip() for line in file]

def prepare_map(_map):
    global ROWS, COLUMNS
    ROWS = len(_map)
    COLUMNS = len(_map[0])
    _map_array = np.zeros((ROWS, COLUMNS))
    for i, row in enumerate(_map):
        _map_array[i] = np.array([c for c in row])
    return _map_array

def find_all(_map, number):
    nodes = []
    for y, y_row in enumerate(_map):
        for x, _ in enumerate(y_row):
            if _map[y][x] == number:
                nodes.append((y, x))
    return nodes

def move(_map, _y, _x, end):
    global ROWS, COLUMNS
    if _y == end[0] and _x == end[1]:
        return True
    for d in [[1, 0], [-1, 0], [0, 1], [0, -1]]:  # direction: right, left, down, up
        j, i = _y + d[0], _x + d[1]
        if 0 <= i < ROWS and 0 <= j < COLUMNS:  # make sure next location is on board
            if _map[j][i] - _map[_y][_x] == 1: # verify that next location is larger by 1
                if move(_map, j, i, end):
                    return True

def part_one(_input):
    _map_array = prepare_map(_input)
    starts = find_all(_map_array, 0)
    ends = find_all(_map_array, 9)
    _sum = 0
    for y, x in starts:
        for end in ends:
            if move(_map_array, y, x, end):
                _sum += 1
    return _sum

def move_part2(_map, _y, _x, end):
    global ROWS, COLUMNS, COUNT
    if _y == end[0] and _x == end[1]:
        COUNT += 1
    for d in [[1, 0], [-1, 0], [0, 1], [0, -1]]:  # direction: right, left, down, up
        j, i = _y + d[0], _x + d[1]
        if 0 <= i < ROWS and 0 <= j < COLUMNS:  # make sure next location is on board
            if _map[j][i] - _map[_y][_x] == 1: # verify that next location is larger by 1
                move_part2(_map, j, i, end)

def part_two(_input):
    global COUNT
    _map_array = prepare_map(_input)
    starts = find_all(_map_array, 0)
    ends = find_all(_map_array, 9)
    _sum = 0
    for y, x in starts:
        for end in ends:
            COUNT = 0
            move_part2(_map_array, y, x, end)
            _sum += COUNT
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
