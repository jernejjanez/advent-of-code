import copy


def prepare_input(file):
    _map = []
    for line in file:
        _map.append(line.strip())
    return _map


def get_rows_columns_to_expand(_map):
    rows = []
    for y in range(len(_map)):
        if "#" not in _map[y]:
            rows.append(y)

    columns = []
    for x in range(len(_map[0])):
        should_add_column = True
        for y in range(len(_map)):
            if _map[y][x] == "#":
                should_add_column = False
                break
        if should_add_column:
            columns.append(x)
    return rows, columns


def calculate_shortest_path(y, x, y1, x1, rows_to_expand, columns_to_expand, multiplier):
    empty_rows = 0
    for row in rows_to_expand:
        if y < y1:
            if y < row < y1:
                empty_rows += 1
        elif y1 < y:
            if y1 < row < y:
                empty_rows += 1

    empty_columns = 0
    for column in columns_to_expand:
        if x < x1:
            if x < column < x1:
                empty_columns += 1
        elif x1 < x:
            if x1 < column < x:
                empty_columns += 1
    return abs(y1 - y) + (empty_rows * (multiplier - 1)) + abs(x1 - x) + (empty_columns * (multiplier - 1))


def part_one(_input):
    rows, columns = get_rows_columns_to_expand(_input)
    _sum = 0
    visited = {}
    for y in range(len(_input)):
        for x in range(len(_input[0])):
            if _input[y][x] == "#":
                for y1 in range(y, len(_input)):
                    for x1 in range(len(_input[0])):
                        if _input[y1][x1] == "#" and (y, x) != (y1, x1) and ((y1, x1), (y, x)) not in visited:
                            visited[((y, x), (y1, x1))] = 0
                            _sum += calculate_shortest_path(y, x, y1, x1, rows, columns, 2)
    return _sum


def part_two(_input):
    rows, columns = get_rows_columns_to_expand(_input)
    _sum = 0
    visited = {}
    for y in range(len(_input)):
        for x in range(len(_input[0])):
            if _input[y][x] == "#":
                for y1 in range(y, len(_input)):
                    for x1 in range(len(_input[0])):
                        if _input[y1][x1] == "#" and (y, x) != (y1, x1) and ((y1, x1), (y, x)) not in visited:
                            visited[((y, x), (y1, x1))] = 0
                            _sum += calculate_shortest_path(y, x, y1, x1, rows, columns, 1000000)
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
