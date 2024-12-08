import copy
import numpy as np
from itertools import combinations


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


def find_all_antennas(_map):
    antennas = {}
    for y, y_row in enumerate(_map):
        for x, _ in enumerate(y_row):
            if _map[y][x] != ".":
                if _map[y][x] in antennas:
                    antennas[_map[y][x]].append((y,x))
                else:
                    antennas[_map[y][x]] = [(y,x)]
    return antennas


def get_coordinates(y1, y2, x1, x2):
    antinode_y = y1
    if y1 < y2:
        antinode_y = y1 - abs(y2 - y1)
    elif y1 > y2:
        antinode_y = y1 + abs(y2 - y1)
    antinode_x = x1
    if x1 < x2:
        antinode_x = x1 - abs(x2 - x1)
    elif x1 > x2:
        antinode_x = x1 + abs(x2 - x1)
    return antinode_y, antinode_x


def get_antinode_location(loc1, loc2):
    antinode1_y, antinode1_x = get_coordinates(loc1[0], loc2[0], loc1[1], loc2[1])
    antinode2_y, antinode2_x = get_coordinates(loc2[0], loc1[0], loc2[1], loc1[1])
    return (antinode1_y, antinode1_x), (antinode2_y, antinode2_x)


def part_one(_input):
    global ROWS, COLUMNS
    unique_locations = []
    _map_array = prepare_map(_input)
    antennas = find_all_antennas(_map_array)
    for key, locations in antennas.items():
        for loc1, loc2 in combinations(locations, 2):
            antinode1, antinode2 = get_antinode_location(loc1, loc2)
            if 0 <= antinode1[1] < ROWS and 0 <= antinode1[0] < COLUMNS:
                if antinode1 not in unique_locations:
                    unique_locations.append(antinode1)
            if 0 <= antinode2[1] < ROWS and 0 <= antinode2[0] < COLUMNS:
                if antinode2 not in unique_locations:
                    unique_locations.append(antinode2)
    return len(unique_locations)


def is_on_map(i, j):
    global ROWS, COLUMNS
    if 0 <= i < ROWS and 0 <= j < COLUMNS:
        return True
    return False


def get_possible_antinodes(y1, y2, x1, x2):
    antinodes = [(y1, x1)]
    while is_on_map(x1, y1):
        antinode_y = y1
        if y1 < y2:
            antinode_y = y1 - abs(y2 - y1)
        elif y1 > y2:
            antinode_y = y1 + abs(y2 - y1)

        antinode_x = x1
        if x1 < x2:
            antinode_x = x1 - abs(x2 - x1)
        elif x1 > x2:
            antinode_x = x1 + abs(x2 - x1)

        x2, y2 = x1, y1
        x1, y1 = antinode_x, antinode_y
        if is_on_map(x1, y1):
            antinodes.append((y1, x1))
    return antinodes


def get_antinode_locations(loc1, loc2):
    antinodes1 = get_possible_antinodes(loc1[0], loc2[0], loc1[1], loc2[1])
    antinodes2 = get_possible_antinodes(loc2[0], loc1[0], loc2[1], loc1[1])
    return antinodes1 + antinodes2


def part_two(_input):
    unique_locations = []
    _map_array = prepare_map(_input)
    antennas = find_all_antennas(_map_array)
    for key, locations in antennas.items():
        for loc1, loc2 in combinations(locations, 2):
            antinodes = get_antinode_locations(loc1, loc2)
            for antinode in antinodes:
                if antinode not in unique_locations:
                    unique_locations.append(antinode)
    return len(unique_locations)


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
