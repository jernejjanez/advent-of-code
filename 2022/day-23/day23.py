import copy

def prepare_input(file):
    return [line.strip() for line in file]

def prepare_dict(_input):
    _dict = {}
    for i, row in enumerate(_input):
        for j, value in enumerate(row):
            _dict[i, j] = ["N", "S", "W", "E"] if value == "#" else None
    return _dict

def should_move(_dict, position):
    x, y = position
    for d in [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]:  # all directions
        i, j = x + d[0], y + d[1]
        if (i, j) in _dict and _dict[(i, j)] is not None:
            return True
    return False

def can_move(_dict, position, direction):
    x, y = position
    adjacent = [-1, 0, 1]
    if direction == "N":
        for adj in adjacent:
            if (x - 1, y + adj) in _dict and _dict[x - 1, y + adj] is not None:
                return False
    if direction == "S":
        for adj in adjacent:
            if (x + 1, y + adj) in _dict and _dict[x + 1, y + adj] is not None:
                return False
    if direction == "W":
        for adj in adjacent:
            if (x + adj, y - 1) in _dict and _dict[x + adj, y - 1] is not None:
                return False
    if direction == "E":
        for adj in adjacent:
            if (x + adj, y + 1) in _dict and _dict[x + adj, y + 1] is not None:
                return False
    return True

def get_new_position(_dict, position, direction):
    x, y = position
    if direction == "N":
        return x - 1, y
    if direction == "S":
        return x + 1, y
    if direction == "W":
        return x, y - 1
    if direction == "E":
        return x, y + 1

def get_number_of_empty_positions(_dict):
    min_x = max(_dict.keys(), key=lambda t: t[0])[0]
    min_y = max(_dict.keys(), key=lambda t: t[1])[1]
    max_x = min(_dict.keys(), key=lambda t: t[0])[0]
    max_y = min(_dict.keys(), key=lambda t: t[1])[1]

    elf_count = 0
    for position, value in _dict.items():
        if value is not None:
            elf_count += 1
            x, y = position
            if x < min_x:
                min_x = x
            if x > max_x:
                max_x = x
            if y < min_y:
                min_y = y
            if y > max_y:
                max_y = y
    max_x += 1
    max_y += 1

    return ((max_x - min_x) * (max_y - min_y)) - elf_count

def part_one(_input):
    _dict = prepare_dict(_input)
    for _ in range(10):
        potential_moves = {}
        for position, directions in _dict.items():
            if directions is not None:
                if should_move(_dict, position):
                    for direction in directions:
                        if can_move(_dict, position, direction):
                            new_value = directions, position
                            new_position = get_new_position(_dict, position, direction)
                            potential_moves[new_position] = None if new_position in potential_moves else new_value
                            break
                first_direction = directions.pop(0)
                directions.append(first_direction)

        for potential_new_position, previous_elf in potential_moves.items():
            if previous_elf is not None:
                previous_directions, previous_position = previous_elf
                _dict[previous_position] = None
                _dict[potential_new_position] = previous_directions

    return get_number_of_empty_positions(_dict)

def get_number_of_elfs(_dict):
    count = 0
    for key, value in _dict.items():
        if value:
            count += 1
    return count

def part_two(_input):
    _dict = prepare_dict(_input)
    number_of_elfs = get_number_of_elfs(_dict)
    stationary_elfs = 0
    i = 0
    while number_of_elfs != stationary_elfs:
        i += 1
        potential_moves = {}
        stationary_elfs = 0
        for position, directions in _dict.items():
            if directions is not None:
                if should_move(_dict, position):
                    for direction in directions:
                        if can_move(_dict, position, direction):
                            new_value = directions, position
                            new_position = get_new_position(_dict, position, direction)
                            potential_moves[new_position] = None if new_position in potential_moves else new_value
                            break
                else:
                    stationary_elfs += 1
                first_direction = directions.pop(0)
                directions.append(first_direction)

        for potential_new_position, previous_elf in potential_moves.items():
            if previous_elf is not None:
                previous_directions, previous_position = previous_elf
                _dict[previous_position] = None
                _dict[potential_new_position] = previous_directions

    return i

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
