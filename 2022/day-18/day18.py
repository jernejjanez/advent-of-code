import copy

def prepare_input(file):
    return [list(map(int, line.strip().split(","))) for line in file]

def part_one(_input):
    number_of_sides = 0
    for item in _input:
        x, y, z = item
        curr_sides = 6
        for compared_item in _input:
            a, b, c = compared_item
            if item == compared_item:
                continue
            if abs(x-a) == 1 and y == b and z == c:
                curr_sides -= 1
            if abs(y-b) == 1 and x == a and z == c:
                curr_sides -= 1
            if abs(z-c) == 1 and y == b and x == a:
                curr_sides -= 1
            if curr_sides == 0:
                break
        number_of_sides += curr_sides

    return number_of_sides

def part_two(_input):
    min_x = min_y = min_z = 100
    max_x = max_y = max_z = 0
    for x, y, z in _input:
        min_x = min(min_x, x)
        min_y = min(min_y, y)
        min_z = min(min_z, z)
        max_x = max(max_x, x)
        max_y = max(max_y, y)
        max_z = max(max_z, z)

    min_x -= 1
    min_y -= 1
    min_z -= 1
    max_x += 1
    max_y += 1
    max_z += 1

    number_of_sides = 0
    exterior_cubes = [[min_x, min_y, min_z]]
    visited = []
    offsets = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
    while len(exterior_cubes) != 0:
        item = exterior_cubes.pop()
        if item not in visited:
            visited.append(item)
            x, y, z = item
            for ox, oy, oz in offsets:
                new_item = [x + ox, y + oy, z + oz]
                if min_x <= x + ox <= max_x and min_y <= y + oy <= max_y and min_z <= z + oz <= max_z:
                    if new_item in _input:
                        number_of_sides += 1
                    else:
                        exterior_cubes.append(new_item)

    return number_of_sides

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
