import copy
import numpy as np

VISITED = []
REGION = []
COUNT = 0
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

def move(_map, _y, _x, char):
    global ROWS, COLUMNS, VISITED, REGION, COUNT
    VISITED.append((_y, _x))
    REGION.append((_y, _x))
    for d in [[1, 0], [-1, 0], [0, 1], [0, -1]]:  # direction: right, left, down, up
        j, i = _y + d[0], _x + d[1]
        if 0 <= i < ROWS and 0 <= j < COLUMNS:
            if _map[j][i] == char:
                if (j, i) not in REGION:
                    move(_map, j, i, char)
            else:
                COUNT += 1
        else:
            COUNT += 1

def part_one(_input):
    global VISITED, REGION, COUNT
    _map_array = prepare_map(_input)
    _sum = 0
    VISITED = []
    for y, y_row in enumerate(_map_array):
        for x, _ in enumerate(y_row):
            if (y, x) not in VISITED:
                REGION = []
                COUNT = 0
                move(_map_array, y, x, _map_array[y][x])
                _sum += len(REGION) * COUNT
    return _sum

def part_two(_input):
    global VISITED, REGION, COUNT
    _map_array = prepare_map(_input)
    _sum = 0
    VISITED = []
    for y, y_row in enumerate(_map_array):
        for x, _ in enumerate(y_row):
            if (y, x) not in VISITED:
                REGION = []
                COUNT = 0
                move(_map_array, y, x, _map_array[y][x])
                _sum += len(REGION) * COUNT
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
