import numpy as np

visited = set()
ROWS = 0
COLUMNS = 0


def check_if_min_recursion(_heightmap, _x, _y):
    global ROWS, COLUMNS, visited

    visited.add(tuple((_x, _y)))
    _heightmap[_x][_y] = 0

    for d in [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]:  # all directions
        i, j = _x + d[0], _y + d[1]
        if 0 <= i < ROWS and 0 <= j < COLUMNS:  # make sure next location is on board
            if _heightmap[i][j] != 0 or tuple((i, j)) not in visited:
                _heightmap[i][j] += 1
                if _heightmap[i][j] > 9:
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

    global visited
    steps = 100
    answer = 0
    for step in range(steps):
        for x, x_row in enumerate(heightmap_array):
            for y, _ in enumerate(x_row):
                if heightmap_array[x][y] != 0 or tuple((x, y)) not in visited:
                    heightmap_array[x][y] += 1
                    if heightmap_array[x][y] > 9:
                        check_if_min_recursion(heightmap_array, x, y)

        answer += np.count_nonzero(heightmap_array == 0)
        visited = set()

    return answer


def part_two(_heightmap):
    heightmap_array = prepare_heightmap_array(_heightmap)

    global visited, ROWS, COLUMNS
    all_flashed = False
    steps = 1
    while not all_flashed:
        for x, x_row in enumerate(heightmap_array):
            for y, _ in enumerate(x_row):
                if heightmap_array[x][y] != 0 or tuple((x, y)) not in visited:
                    heightmap_array[x][y] += 1
                    if heightmap_array[x][y] > 9:
                        check_if_min_recursion(heightmap_array, x, y)

        if np.count_nonzero(heightmap_array == 0) == ROWS * COLUMNS:
            all_flashed = True
        else:
            steps += 1
        visited = set()

    return steps


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
