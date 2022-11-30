import copy
from queue import PriorityQueue


def prepare_input(file):
    return [list(map(int, list(line.strip()))) for line in file]


def prepare_entire_cave(_input):
    entire_cave = []
    for row in _input:
        entire_cave_row = copy.deepcopy(row)
        temp_row = copy.deepcopy(row)
        for i in range(4):
            increased_row = []
            for item in temp_row:
                if item == 9:
                    increased_row.append(1)
                else:
                    increased_row.append(item + 1)
            temp_row = increased_row
            entire_cave_row += increased_row
        entire_cave.append(entire_cave_row)

    new_cave_segment = copy.deepcopy(entire_cave)
    for i in range(4):
        temp_segment = []
        for row in new_cave_segment:
            increased_row = []
            for item in row:
                if item == 9:
                    increased_row.append(1)
                else:
                    increased_row.append(item + 1)
            temp_segment.append(increased_row)
            new_cave_segment = temp_segment
            entire_cave.append(increased_row)

    return entire_cave


def find_lowest_risk(cave_map, _start, _end):
    frontier = PriorityQueue()
    frontier.put((0, _start))

    came_from = {_start: None}
    risk_so_far = {_start: 0}
    offsets = ((1, 0), (0, 1), (-1, 0), (0, -1))
    pos = None

    while not frontier.empty():
        pos = frontier.get()[1]

        if pos == _end:
            break

        for offset in offsets:
            new_pos = (pos[0] + offset[0], pos[1] + offset[1])
            if 0 <= new_pos[0] < len(cave_map[0]) and 0 <= new_pos[1] < len(cave_map):
                new_risk = risk_so_far[pos] + cave_map[new_pos[0]][new_pos[1]]
                if new_pos not in came_from or new_risk < risk_so_far[new_pos]:
                    risk_so_far[new_pos] = new_risk
                    priority = new_risk + abs(new_pos[0] - _end[0]) + abs(new_pos[1] - _end[1])
                    frontier.put((priority, new_pos))
                    came_from[new_pos] = pos

    return risk_so_far[pos]


def part_one(risk_level_map):
    start = (0, 0)
    end = (len(risk_level_map) - 1, len(risk_level_map[0]) - 1)

    return find_lowest_risk(risk_level_map, start, end)


def part_two(_input):
    entire_cave = prepare_entire_cave(_input)

    start = (0, 0)
    end = (len(entire_cave) - 1, len(entire_cave[0]) - 1)

    return find_lowest_risk(entire_cave, start, end)


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        _input = prepare_input(f)

    answer1 = part_one(_input)
    print("Part one:")
    print("Answer: {}".format(int(answer1)))
    print()
    answer2 = part_two(_input)
    print("Part two:")
    print("Answer: {}".format(int(answer2)))
