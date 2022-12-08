import copy
import numpy as np

ROWS = 0
COLUMNS = 0

def prepare_input(file):
    return [list(map(int, list(line.strip()))) for line in file]

def prepare_map(_map):
    global ROWS, COLUMNS
    ROWS = len(_map)
    COLUMNS = len(_map[0])
    _map_array = np.zeros((ROWS, COLUMNS))
    for i, row in enumerate(_map):
        _map_array[i] = np.array(row)
    return _map_array

def is_visible_up(_heightmap, _x, _y):
    curr = _heightmap[_x][_y]
    while _y > 0:
        for d in [[0, -1]]:
            _x, _y = _x + d[0], _y + d[1]
            if _heightmap[_x][_y] >= curr:
                return 0
    return 1

def is_visible_down(_heightmap, _x, _y):
    global COLUMNS
    curr = _heightmap[_x][_y]
    while _y < COLUMNS - 1:
        for d in [[0, 1]]:
            _x, _y = _x + d[0], _y + d[1]
            if _heightmap[_x][_y] >= curr:
                return 0
    return 1

def is_visible_left(_heightmap, _x, _y):
    curr = _heightmap[_x][_y]
    while _x > 0:
        for d in [[-1, 0]]:
            _x, _y = _x + d[0], _y + d[1]
            if _heightmap[_x][_y] >= curr:
                return 0
    return 1

def is_visible_right(_heightmap, _x, _y):
    global ROWS
    curr = _heightmap[_x][_y]
    while _x < ROWS - 1:
        for d in [[1, 0]]:
            _x, _y = _x + d[0], _y + d[1]
            if _heightmap[_x][_y] >= curr:
                return 0
    return 1

def is_visible(_heightmap, _x, _y):
    global ROWS, COLUMNS

    if _x == 0:
        return 1
    if _x == ROWS - 1:
        return 1
    if _y == 0:
        return 1
    if _y == COLUMNS - 1:
        return 1

    up = is_visible_up(_heightmap, _x, _y)
    down = is_visible_down(_heightmap, _x, _y)
    left = is_visible_left(_heightmap, _x, _y)
    right = is_visible_right(_heightmap, _x, _y)
    return 1 if up + down + left + right > 0 else 0

def part_one(_input):
    _map = prepare_map(_input)
    answer = 0
    for x, x_row in enumerate(_map):
        for y, _ in enumerate(x_row):
            answer += is_visible(_map, x, y)
    return answer

def get_scenic_score_up(_heightmap, _x, _y):
    curr = _heightmap[_x][_y]
    ans = 0
    while _y > 0:
        for d in [[0, -1]]:
            _x, _y = _x + d[0], _y + d[1]
            if _heightmap[_x][_y] >= curr:
                return ans + 1
            else:
                ans += 1
    return ans

def get_scenic_score_down(_heightmap, _x, _y):
    global COLUMNS
    curr = _heightmap[_x][_y]
    ans = 0
    while _y < COLUMNS - 1:
        for d in [[0, 1]]:
            _x, _y = _x + d[0], _y + d[1]
            if _heightmap[_x][_y] >= curr:
                return ans + 1
            else:
                ans += 1
    return ans

def get_scenic_score_left(_heightmap, _x, _y):
    curr = _heightmap[_x][_y]
    ans = 0
    while _x > 0:
        for d in [[-1, 0]]:
            _x, _y = _x + d[0], _y + d[1]
            if _heightmap[_x][_y] >= curr:
                return ans + 1
            else:
                ans += 1
    return ans

def get_scenic_score_right(_heightmap, _x, _y):
    global ROWS
    curr = _heightmap[_x][_y]
    ans = 0
    while _x < ROWS - 1:
        for d in [[1, 0]]:
            _x, _y = _x + d[0], _y + d[1]
            if _heightmap[_x][_y] >= curr:
                return ans + 1
            else:
                ans += 1
    return ans

def get_scenic_score(_heightmap, _x, _y):
    up = get_scenic_score_up(_heightmap, _x, _y)
    down = get_scenic_score_down(_heightmap, _x, _y)
    left = get_scenic_score_left(_heightmap, _x, _y)
    right = get_scenic_score_right(_heightmap, _x, _y)
    return up * down * left * right

def part_two(_input):
    _map = prepare_map(_input)
    answer = []
    for x, x_row in enumerate(_map):
        for y, _ in enumerate(x_row):
            answer.append(get_scenic_score(_map, x, y))
    return max(answer)


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
