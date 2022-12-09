import copy

visited = set()
d_dict = {
    "U": [0, -1],
    "D": [0, 1],
    "L": [-1, 0],
    "R": [1, 0]
}

def string_to_int(string_or_int):
    try:
        return int(string_or_int)
    except ValueError:
        return string_or_int

def prepare_input(file):
    return [list(map(string_to_int, list(line.split()))) for line in file]

def is_neighbour(h_x, h_y, t_x, t_y):
    for d in [[0, 0], [1, 0], [1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]:  # all directions
        i, j = t_x + d[0], t_y + d[1]
        if i == h_x and j == h_y:
            return True
    return False

def is_neighbour_manhattan(h_x, h_y, t_x, t_y):
    for d in [[0, 0], [1, 0], [1, 0], [-1, 0], [0, 1], [0, -1]]:  # direction: right, left, down, up
        i, j = t_x + d[0], t_y + d[1]
        if i == h_x and j == h_y:
            return True
    return False

def move_tail(h_x, h_y, t_x, t_y):
    for d in [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]:  # all directions
        i, j = t_x + d[0], t_y + d[1]
        if is_neighbour_manhattan(h_x, h_y, i, j):
            return i, j
    return move_tail_all_dir(h_x, h_y, t_x, t_y)

def move_tail_all_dir(h_x, h_y, t_x, t_y):
    for d in [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]:  # all directions
        i, j = t_x + d[0], t_y + d[1]
        if is_neighbour(h_x, h_y, i, j):
            return i, j

def part_one(_input):
    global visited
    h_x = 0
    h_y = 0
    t_x = 0
    t_y = 0
    visited.add(tuple((t_x, t_y)))
    for direction, steps in _input:
        for _ in range(steps):
            for d in [d_dict[direction]]:
                h_x, h_y = h_x + d[0], h_y + d[1]
                if is_neighbour(h_x, h_y, t_x, t_y):
                    continue
                else:
                    t_x, t_y = move_tail(h_x, h_y, t_x, t_y)
                    if tuple((t_x, t_y)) not in visited:
                        visited.add(tuple((t_x, t_y)))
    return len(visited)

def part_two(_input):
    global visited
    h_x = 0
    h_y = 0
    t_x = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    t_y = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    visited = set()
    visited.add(tuple((0, 0)))
    for direction, steps in _input:
        for _ in range(steps):
            for d in [d_dict[direction]]:
                h_x, h_y = h_x + d[0], h_y + d[1]
                curr_x = h_x
                curr_y = h_y
                for curr_tail in range(len(t_x)):
                    if is_neighbour(curr_x, curr_y, t_x[curr_tail], t_y[curr_tail]):
                        pass
                    else:
                        new_x, new_y = move_tail(curr_x, curr_y, t_x[curr_tail], t_y[curr_tail])
                        t_x[curr_tail] = new_x
                        t_y[curr_tail] = new_y
                        if curr_tail == 8 and tuple((t_x[curr_tail], t_y[curr_tail])) not in visited:
                            visited.add(tuple((t_x[curr_tail], t_y[curr_tail])))
                    curr_x, curr_y = t_x[curr_tail], t_y[curr_tail]
    return len(visited)

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
