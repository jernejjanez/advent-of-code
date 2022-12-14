import copy
import numpy as np

global_y = 0

def prepare_input(file):
    return [line.strip().split(" -> ") for line in file]

def prepare_map(size):
    _map_array = np.zeros((size, size), str)
    return _map_array

def draw_vertical(_map, x, y1, y2):
    if y1 == y2:
        pass
    else:
        for y in range(min(y1, y2), max(y1, y2) + 1):
            _map[y][x] = "#"

def draw_horizontal(_map, x1, x2, y):
    if x1 == x2:
        pass
    else:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            _map[y][x] = "#"

def set_settled_sand_position(_map, x, y, max_y):
    global global_y
    move_down = _map[y + 1][x]
    move_down_left = _map[y + 1][x - 1]
    move_down_right = _map[y + 1][x + 1]
    not_settled = True
    while not_settled:
        if y > max_y:
            global_y = y
            return False
        if move_down != "#" and move_down != "o":
            not_settled = set_settled_sand_position(_map, x, y + 1, max_y)
        elif move_down_left != "#" and move_down_left != "o":
            not_settled = set_settled_sand_position(_map, x - 1, y + 1, max_y)
        elif move_down_right != "#" and move_down_right != "o":
            not_settled = set_settled_sand_position(_map, x + 1, y + 1, max_y)
        else:
            _map[y][x] = "o"
            return False

def drop_sand(_map, start_x, start_y, max_y):
    global global_y
    curr_x = start_x
    curr_y = start_y
    number_of_sands = 0
    while global_y <= max_y and _map[curr_y][curr_x] != "o":
        if _map[curr_y][curr_x] == "":
            curr_y += 1
        if _map[curr_y][curr_x] == "#" or _map[curr_y][curr_x] == "o":
            set_settled_sand_position(_map, curr_x, curr_y - 1, max_y)
            if global_y <= max_y:
                number_of_sands += 1
                curr_x = start_x
                curr_y = start_y

    return number_of_sands

def draw_floor(_map, y, size):
    for x in range(0, size):
        _map[y][x] = "#"

def part_one(_input):
    _map = prepare_map(1000)
    max_y = 0
    for c in _input:
        x1, y1 = list(map(int, c.pop(0).split(",")))
        max_y = max(y1, max_y)
        while len(c) != 0:
            x2, y2 = list(map(int, c.pop(0).split(",")))
            max_y = max(y2, max_y)
            draw_vertical(_map, x1, y1, y2)
            draw_horizontal(_map, x1, x2, y1)
            x1, y1 = x2, y2

    result = drop_sand(_map, 500, 0, max_y)
    return result

def part_two(_input):
    global global_y
    global_y = 0
    size = 1000
    _map = prepare_map(size)
    max_y = 0
    for c in _input:
        x1, y1 = list(map(int, c.pop(0).split(",")))
        max_y = max(y1, max_y)
        while len(c) != 0:
            x2, y2 = list(map(int, c.pop(0).split(",")))
            max_y = max(y2, max_y)
            draw_vertical(_map, x1, y1, y2)
            draw_horizontal(_map, x1, x2, y1)
            x1, y1 = x2, y2

    draw_floor(_map, max_y + 2, size)
    result = drop_sand(_map, 500, 0, max_y + 2)
    return result

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
