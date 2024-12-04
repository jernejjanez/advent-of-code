import copy
import numpy as np


ROWS = 0
COLUMNS = 0
WORD = "XMAS"


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


def find_number_of_xmas(_map, _y, _x, idx, move):
    global ROWS, COLUMNS, WORD
    if _map[_y][_x] != WORD[idx]:
        return 0
    else:
        if _map[_y][_x] == WORD[idx] == "S":
            return 1
        i, j = _x + move[0], _y + move[1]
        if 0 <= i < ROWS and 0 <= j < COLUMNS:  # make sure next location is on board
            if _map[j][i] == WORD[idx+1]:
                return find_number_of_xmas(_map, j, i, idx+1, move)
    return 0


def part_one(_input):
    global ROWS, COLUMNS
    number_of_xmas = 0
    numpy_map = prepare_numpy_map(_input)
    for start_y in range(COLUMNS):
        for start_x in range(ROWS):
            if numpy_map[start_y][start_x] == "X":
                for d in [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]:  # all directions
                    number_of_xmas += find_number_of_xmas(numpy_map, start_y, start_x, 0, d)
    return number_of_xmas


def is_diagonal_correct(_map, _y, _x, move1, move2):
    global ROWS, COLUMNS
    i1, j1 = _x + move1[0], _y + move1[1]
    i2, j2 = _x + move2[0], _y + move2[1]
    if 0 <= i1 < ROWS and 0 <= j1 < COLUMNS and 0 <= i2 < ROWS and 0 <= j2 < COLUMNS:
        if (_map[j1][i1] == "M" and _map[j2][i2] == "S") or (_map[j1][i1] == "S" and _map[j2][i2] == "M"):
            return True
    return False


def find_number_of_xmas_x_shapes(_map, _y, _x):
    if is_diagonal_correct(_map, _y, _x, [1, 1], [-1, -1]) and is_diagonal_correct(_map, _y, _x, [1, -1], [-1, 1]):
        return 1
    return 0


def part_two(_input):
    global ROWS, COLUMNS
    number_of_xmas = 0
    numpy_map = prepare_numpy_map(_input)
    for start_y in range(COLUMNS):
        for start_x in range(ROWS):
            if numpy_map[start_y][start_x] == "A":
                number_of_xmas += find_number_of_xmas_x_shapes(numpy_map, start_y, start_x)
    return number_of_xmas


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
