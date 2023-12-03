import copy


def find_number(line, index):
    number = line[index]
    left_index = index - 1
    right_index = index + 1
    while left_index >= 0 and line[left_index].isdigit():
        number = line[left_index] + number
        left_index -= 1
    while right_index < len(line) and line[right_index].isdigit():
        number += line[right_index]
        right_index += 1
    return number


def prepare_input(file):
    schematic = []
    for line in file:
        schematic_line = []
        line = line.strip()
        for i, c in enumerate(line):
            if c.isdigit():
                schematic_line.append(find_number(line, i))
            else:
                schematic_line.append(c)
        schematic.append(schematic_line)
    return schematic


def find_whole_number(scheme, visited, _x, _y):
    visited.append((_y, _x))
    left_index = _x - 1
    right_index = _x + 1
    while left_index >= 0 and scheme[_y][left_index].isdigit():
        visited.append((_y, left_index))
        left_index -= 1
    while right_index < len(scheme[_y]) and scheme[_y][right_index].isdigit():
        visited.append((_y, right_index))
        right_index += 1
    return visited


def get_adjacent_numbers(scheme, visited, _x, _y):
    _sum = 0
    for d in [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]:  # all directions
        i, j = _y + d[0], _x + d[1]
        if scheme[i][j].isdigit() and tuple((i, j)) not in visited:
            _sum += int(scheme[i][j])
            visited = find_whole_number(scheme, visited, j, i)
    return _sum, visited


def part_one(_input):
    _sum = 0
    visited = []
    for y, schematic_line in enumerate(_input):
        for x, c in enumerate(schematic_line):
            if not c.isdigit() and c != ".":
                temp_sum, temp_visited = get_adjacent_numbers(_input, visited, x, y)
                visited = temp_visited
                _sum += temp_sum
    return _sum


def get_gear_ratio(scheme, visited, _x, _y):
    gear_ratio = 1
    number_of_adjacent_numbers = 0
    for d in [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]:  # all directions
        i, j = _y + d[0], _x + d[1]
        if scheme[i][j].isdigit() and tuple((i, j)) not in visited:
            gear_ratio *= int(scheme[i][j])
            visited = find_whole_number(scheme, visited, j, i)
            number_of_adjacent_numbers += 1
    return (gear_ratio, visited) if number_of_adjacent_numbers == 2 else (0, visited)


def part_two(_input):
    _sum = 0
    visited = []
    for y, schematic_line in enumerate(_input):
        for x, c in enumerate(schematic_line):
            if not c.isdigit() and c == "*":
                temp_sum, temp_visited = get_gear_ratio(_input, visited, x, y)
                visited = temp_visited
                _sum += temp_sum
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
