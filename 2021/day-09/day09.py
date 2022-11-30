import numpy as np

size = 0
visited = set()
ROWS = 0
COLUMNS = 0


def check_if_min(_heightmap, _x, _y):
    current_height = _heightmap[_x][_y]
    if _x + 1 != len(_heightmap) and current_height >= _heightmap[_x + 1][_y]:
        return 0
    elif _x - 1 != -1 and current_height >= _heightmap[_x - 1][_y]:
        return 0
    elif _y + 1 != len(_heightmap[0]) and current_height >= _heightmap[_x][_y + 1]:
        return 0
    elif _y - 1 != -1 and current_height >= _heightmap[_x][_y - 1]:
        return 0
    else:
        return current_height + 1


def check_if_min_recursion(_heightmap, _x, _y):
    global ROWS, COLUMNS, visited, size

    visited.add(tuple((_x, _y)))
    size += 1

    for d in [[1, 0], [-1, 0], [0, 1], [0, -1]]:  # direction: right, left, down, up
        i, j = _x + d[0], _y + d[1]
        if 0 <= i < ROWS and 0 <= j < COLUMNS:  # make sure next location is on board
            if _heightmap[i][j] != 9:  # verify that next location is not a '9'
                if tuple((i, j)) not in visited:  # verify that we have not visited the next location already
                    check_if_min_recursion(_heightmap, i, j)


def prepare_heightmap_array(_heightmap):
    global ROWS, COLUMNS
    ROWS = len(_heightmap)
    COLUMNS = len(_heightmap[0])
    _heightmap_array = np.zeros((ROWS, COLUMNS))
    for i, row in enumerate(_heightmap):
        _heightmap_array[i] = np.array(row)

    return _heightmap_array


def part_one(_heightmap):
    heightmap_array = prepare_heightmap_array(_heightmap)

    answer = 0
    for x, x_row in enumerate(heightmap_array):
        for y, _ in enumerate(x_row):
            answer += check_if_min(heightmap_array, x, y)

    return answer


def part_two(_heightmap):
    heightmap_array = prepare_heightmap_array(_heightmap)

    global visited, size
    sizes = []
    for x, x_row in enumerate(heightmap_array):
        for y, _ in enumerate(x_row):
            if tuple((x, y)) not in visited and heightmap_array[x][y] != 9:
                check_if_min_recursion(heightmap_array, x, y)
                sizes.append(size)
                size = 0

    sizes = sorted(sizes, reverse=True)

    return sizes[0] * sizes[1] * sizes[2]


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        heightmap = [list(map(int, list(line.strip()))) for line in f]

    answer1 = part_one(heightmap)
    print("Part one:")
    print("Answer: {}".format(int(answer1)))
    print()
    answer2 = part_two(heightmap)
    print("Part two:")
    print("Answer: {}".format(answer2))
