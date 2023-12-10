import copy
import math

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


def find_possible_neighbours(_map, _y, _x):
    possible_neighbours = []
    for d in [[1, 0], [-1, 0], [0, 1], [0, -1]]:  # direction: right, left, up, down
        i, j = _x + d[0], _y + d[1]
        if 0 <= i < ROWS and 0 <= j < COLUMNS:  # make sure next location is on board
            if _map[j][i] == ".":
                continue
            elif _map[j][i] == "|" and (d == [0, 1] or d == [0, -1]):
                possible_neighbours.append((j, i))
            elif _map[j][i] == "-" and (d == [1, 0] or d == [-1, 0]):
                possible_neighbours.append((j, i))
            elif _map[j][i] == "L" and (d == [0, 1] or d == [-1, 0]):
                possible_neighbours.append((j, i))
            elif _map[j][i] == "J" and (d == [0, 1] or d == [1, 0]):
                possible_neighbours.append((j, i))
            elif _map[j][i] == "7" and (d == [0, -1] or d == [1, 0]):
                possible_neighbours.append((j, i))
            elif _map[j][i] == "F" and (d == [0, -1] or d == [-1, 0]):
                possible_neighbours.append((j, i))
    return possible_neighbours


def find_next_position(_map, position, move):
    _y, _x = position
    if _map[position] == "|":
        if move == [1, 0]:
            return (_y + 1, _x), [1, 0]
        else:
            return (_y - 1, _x), [-1, 0]
    elif _map[position] == "-":
        if move == [0, 1]:
            return (_y, _x + 1), [0, 1]
        else:
            return (_y, _x - 1), [0, -1]
    elif _map[position] == "L":
        if move == [1, 0]:
            return (_y, _x + 1), [0, 1]
        else:
            return (_y - 1, _x), [-1, 0]
    elif _map[position] == "J":
        if move == [1, 0]:
            return (_y, _x - 1), [0, -1]
        else:
            return (_y - 1, _x), [-1, 0]
    elif _map[position] == "7":
        if move == [-1, 0]:
            return (_y, _x - 1), [0, -1]
        else:
            return (_y + 1, _x), [1, 0]
    elif _map[position] == "F":
        if move == [-1, 0]:
            return (_y, _x + 1), [0, 1]
        else:
            return (_y + 1, _x), [1, 0]


def part_one(_input):
    numpy_map = prepare_numpy_map(_input)
    start_y, start_x = np.where(numpy_map == "S")
    start_y = start_y[0]
    start_x = start_x[0]
    neighbours = find_possible_neighbours(numpy_map, start_y, start_x)
    next_position = neighbours[0]
    move = [neighbours[0][0] - start_y, neighbours[0][1] - start_x]
    number_of_moves = 0
    while numpy_map[next_position] != "S":
        next_position, move = find_next_position(numpy_map, next_position, move)
        number_of_moves += 1
    return math.ceil(number_of_moves / 2)


def part_two(_input):
    numpy_map = prepare_numpy_map(_input)
    start_y, start_x = np.where(numpy_map == "S")
    start_y = start_y[0]
    start_x = start_x[0]
    neighbours = find_possible_neighbours(numpy_map, start_y, start_x)
    next_position = neighbours[0]
    move = [neighbours[0][0] - start_y, neighbours[0][1] - start_x]
    number_of_moves = 1
    dists = {(start_y, start_x): 0, (next_position[0], next_position[1]): 1}
    while numpy_map[next_position] != "S":
        next_position, move = find_next_position(numpy_map, next_position, move)
        number_of_moves += 1
        dists[next_position] = number_of_moves

    # Replace start with actual pipe for part 2 to work
    numpy_map[numpy_map == "S"] = "L"

    # Imagine a person standing on one of the squares, and they shoot a laser in any direction except for the four
    # cardinal directions (to prevent the collinearity problem). Diagonally, say. Now trace that laser starting at the
    # square shooting it until it exits the field. If it's inside the shape, it will cross the boundary an odd number
    # of times, if it's outside it will cross an even number of times. Be careful if it hits a corner from the outside:
    # it either crosses it twice, or zero times.

    # The simplest example is if the boundary is just a circle. If you're inside the circle and shoot your laser,
    # it will hit it once, on its way out. If you're outside the circle it will hit it either zero times (misses the
    # circle entirely) or two times (hit once going in, hit once going out). The corner case is if your laser is
    # EXACTLY tangent to the circle, then it hits it "once" (but really twice, from a mathematical perspective the
    # tangent point is two hits).

    # It's intuitive for circles, but the concept generalizes to ANY enclosed shape: if you hit the shape twice,
    # you've "gone in" and then "gone out". But if you were inside from the beginning, there's an extra "gone out",
    # so the number of crossings is odd. You just have to be careful about tangents and collinearity.
    inside_count = 0
    for (y, x), value in np.ndenumerate(numpy_map):
        if (y, x) in dists:
            continue

        crosses = 0
        x2, y2 = x, y
        while x2 < ROWS and y2 < COLUMNS:
            c2 = numpy_map[y2][x2]
            if (y2, x2) in dists and c2 != "L" and c2 != "7":
                crosses += 1
            x2 += 1
            y2 += 1

        if crosses % 2 == 1:
            inside_count += 1
    return inside_count


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
