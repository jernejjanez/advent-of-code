import copy
import numpy as np

ROWS = 0
COLUMNS = 0
alphabet_values = {}

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

def prepare_alphabet_values():
    global alphabet_values
    for i in range(97, 123):
        alphabet_values[chr(i)] = i
    alphabet_values[chr(69)] = 122
    alphabet_values[chr(83)] = 97

def print_map(_map, steps):
    for x, x_row in enumerate(_map):
        for y, _ in enumerate(x_row):
            if (x, y) in steps:
                print(_map[x][y].upper(), end="")
            else:
                print(_map[x][y], end="")
        print()

def find_node(_map, char):
    for x, x_row in enumerate(_map):
        for y, _ in enumerate(x_row):
            if _map[x][y] == char:
                return x, y

def find_all_nodes_with_char(_map, char):
    positions = []
    for x, x_row in enumerate(_map):
        for y, _ in enumerate(x_row):
            if _map[x][y] == char:
                positions.append((x, y))
    return positions

def breadth_first_search(cave_map, _start, _end):
    global alphabet_values
    queue = [_start]
    came_from = {_start: None}
    offsets = ((1, 0), (0, 1), (-1, 0), (0, -1))
    while not len(queue) == 0:
        pos = queue.pop(0)
        if pos == _end:
            steps = 0
            steps_array = [_end]
            while pos != _start:
                pos = came_from[pos]
                steps_array.append(pos)
                steps += 1
            # print_map(cave_map, steps_array)
            return steps

        for offset in offsets:
            new_pos = (pos[0] + offset[0], pos[1] + offset[1])
            if 0 <= new_pos[0] < len(cave_map) and 0 <= new_pos[1] < len(cave_map[0]):
                can_move = True if alphabet_values[cave_map[pos[0]][pos[1]]] - \
                                   alphabet_values[cave_map[new_pos[0]][new_pos[1]]] >= -1 else False
                if new_pos not in came_from and can_move:
                    queue.append(new_pos)
                    came_from[new_pos] = pos

    return 999999

def part_one(_input):
    prepare_alphabet_values()
    _map_array = prepare_map(_input)

    start = find_node(_map_array, "S")
    end = find_node(_map_array, "E")
    return breadth_first_search(_map_array, start, end)

def part_two(_input):
    prepare_alphabet_values()
    _map_array = prepare_map(_input)

    start_positions_array = find_all_nodes_with_char(_map_array, "a")
    start = find_node(_map_array, "S")
    start_positions_array.append(start)
    end = find_node(_map_array, "E")
    result = []
    for start_position in start_positions_array:
        result.append(breadth_first_search(_map_array, start_position, end))
    return min(result)

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
