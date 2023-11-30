import copy


def prepare_input(file):
    are_instructions = False
    _map = []
    map_width = 0
    instructions = ""
    for line in file:
        if line == "\n":
            are_instructions = True
            continue
        if are_instructions:
            instructions = line + "E"
        else:
            _map.append(line[0:-1])
            if map_width < len(line[0:-1]):
                map_width = len(line[0:-1])
    return _map, map_width, instructions


def prepare_dict(_input, width):
    _dict = {}
    for i, row in enumerate(_input):
        for j in range(width):
            _dict[i, j] = "out" if j >= len(row) or row[j] == " " else "wall" if row[j] == "#" else "open"
    return _dict


def get_starting_position(_dict, width):
    for j in range(width):
        if _dict[(0, j)] == "open":
            return 0, j


def move(_dict, position, number, direction):
    x, y = position
    if direction == "right":
        for step in range(number):
            y += 1
            new_position = x, y
            if new_position not in _dict or _dict[new_position] == "out":
                temp_y = 0
                new_position = x, temp_y
                while _dict[new_position] != "open" and _dict[new_position] != "wall":
                    temp_y += 1
                    new_position = x, temp_y
                if _dict[new_position] == "wall":
                    return x, y - 1
                elif _dict[new_position] == "open":
                    y = temp_y
            elif _dict[new_position] == "wall":
                return x, y - 1
        return x, y
    if direction == "down":
        for step in range(number):
            x += 1
            new_position = x, y
            if new_position not in _dict or _dict[new_position] == "out":
                temp_x = 0
                new_position = temp_x, y
                while _dict[new_position] != "open" and _dict[new_position] != "wall":
                    temp_x += 1
                    new_position = temp_x, y
                if _dict[new_position] == "wall":
                    return x - 1, y
                elif _dict[new_position] == "open":
                    x = temp_x
            elif _dict[new_position] == "wall":
                return x - 1, y
        return x, y
    if direction == "left":
        for step in range(number):
            y -= 1
            new_position = x, y
            if new_position not in _dict or _dict[new_position] == "out":
                temp_y = max(_dict.keys(), key=lambda t: t[1])[1]
                new_position = x, temp_y
                while _dict[new_position] != "open" and _dict[new_position] != "wall":
                    temp_y -= 1
                    new_position = x, temp_y
                if _dict[new_position] == "wall":
                    return x, y + 1
                elif _dict[new_position] == "open":
                    y = temp_y
            elif _dict[new_position] == "wall":
                return x, y + 1
        return x, y
    if direction == "up":
        for step in range(number):
            x -= 1
            new_position = x, y
            if new_position not in _dict or _dict[new_position] == "out":
                temp_x = max(_dict.keys(), key=lambda t: t[0])[0]
                new_position = temp_x, y
                while _dict[new_position] != "open" and _dict[new_position] != "wall":
                    temp_x -= 1
                    new_position = temp_x, y
                if _dict[new_position] == "wall":
                    return x + 1, y
                elif _dict[new_position] == "open":
                    x = temp_x
            elif _dict[new_position] == "wall":
                return x + 1, y
        return x, y


def rotate(directions, letter):
    if letter == "R":
        directions.append(directions.pop(0))
    elif letter == "L":
        directions.insert(0, directions.pop())
    return directions


def get_sum(row, column, facing):
    facing_value = 0 if facing == "right" else 1 if facing == "down" else 2 if facing == "left" else 3
    return (1000 * row) + (4 * column) + facing_value


def part_one(_input):
    raw_map, map_width, instructions = _input
    _dict = prepare_dict(raw_map, map_width)
    position = get_starting_position(_dict, map_width)
    directions = ["right", "down", "left", "up"]

    number_string = ""
    for char in instructions:
        if char == "E":
            number = int(number_string)
            position = move(_dict, position, number, directions[0])
        elif char == "R" or char == "L":
            number = int(number_string)
            position = move(_dict, position, number, directions[0])
            directions = rotate(directions, char)
            number_string = ""
        else:
            number_string += char
    return get_sum(position[0] + 1, position[1] + 1, directions[0])


def part_two(_input):
    return 0


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
