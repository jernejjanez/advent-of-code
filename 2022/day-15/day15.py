import copy
import numpy as np
# import ast

def prepare_input(file):
    return [line.strip().split(": closest beacon is at ") for line in file]

def prepare_map(size):
    _map_array = np.zeros((size, size), str)
    return _map_array

def breadth_first_search(beacon_positions, result_positions, visited_positions, _start, _end, target_row):
    queue = [_start]
    came_from = {_start: None}
    offsets = ((1, 0), (0, 1), (-1, 0), (0, -1))
    result = 0
    while not len(queue) == 0:
        pos = queue.pop(0)
        if pos == _end:
            # steps = 0
            # steps_array = [_end]
            # while pos != _start:
            #     pos = came_from[pos]
            #     steps_array.append(pos)
            #     steps += 1
            # print_map(cave_map, steps_array)
            return result_positions, visited_positions

        for offset in offsets:
            new_pos = (pos[0] + offset[0], pos[1] + offset[1])
            if new_pos not in came_from:
                queue.append(new_pos)
                came_from[new_pos] = pos
                if new_pos[1] == target_row and new_pos not in beacon_positions and new_pos not in result_positions and new_pos not in visited_positions:
                    result_positions.append(new_pos)
                    visited_positions.append(new_pos)
                    result += 1

    return result_positions, visited_positions

def part_one(_input):
    result = 0
    sensors = []
    beacons = []
    max_x = 0
    min_x = 0
    max_y = 0
    min_y = 0
    for sensor, beacon in _input:
        s_x, s_y = sensor.split("Sensor at ")[1].split(", ")
        b_x, b_y = beacon.split(", ")
        s_x = int(s_x[2:])
        s_y = int(s_y[2:])
        b_x = int(b_x[2:])
        b_y = int(b_y[2:])
        max_x = max(max_x, s_x, b_x)
        min_x = min(min_x, s_x, b_x)
        max_y = max(max_y, s_y, b_y)
        min_y = min(min_y, s_y, b_y)
        sensors.append((s_x, s_y))
        beacons.append((b_x, b_y))

    result_positions = []
    visited_positions = []
    # target_y = 10
    target_y = 2000000
    temp = set()
    beacons_on_target_count = 0
    beacons_on_target = []
    for s, b in zip(sensors, beacons):
        if b[1] == target_y and b not in beacons_on_target:
            beacons_on_target_count += 1
            beacons_on_target.append(b)
        y_path = abs(s[1] - b[1])
        x_path = abs(s[0] - b[0])
        path = x_path + y_path
        if path >= abs(s[1] - target_y):
            y_steps = abs(target_y - s[1])
            x_steps = path - y_steps
            temp.add((s[0], x_steps))
            # for step in range(x_steps+1):
            #     if (s[0] + step, target_y) not in beacons and (s[0] + step, target_y) not in visited_positions:
            #         visited_positions.append((s[0] + step, target_y))
            #     if (s[0] - step, target_y) not in beacons and (s[0] - step, target_y) not in visited_positions:
            #         visited_positions.append((s[0] - step, target_y))
        # result_positions, visited_positions = breadth_first_search(beacons, result_positions, visited_positions, s, b, 10)
        # result_positions, visited_positions = breadth_first_search(beacons, result_positions, visited_positions, s, b, 2000000)

    right_position = None
    left_position = None
    for pos, steps in temp:
        if right_position is None or pos + steps > right_position:
            right_position = pos + steps
        if left_position is None or pos - steps < left_position:
            left_position = pos - steps

    return right_position + abs(left_position) - beacons_on_target_count + 1

def part_two(_input):
    result = 0
    sensors = []
    beacons = []
    max_x = 0
    min_x = 0
    max_y = 0
    min_y = 0
    min_coordinates = 0
    max_coordinates = 20
    target_y = 10
    # target_y = 2000000
    for sensor, beacon in _input:
        s_x, s_y = sensor.split("Sensor at ")[1].split(", ")
        b_x, b_y = beacon.split(", ")
        s_x = int(s_x[2:])
        s_y = int(s_y[2:])
        b_x = int(b_x[2:])
        b_y = int(b_y[2:])
        max_x = max(max_x, s_x, b_x)
        min_x = min(min_x, s_x, b_x)
        max_y = max(max_y, s_y, b_y)
        min_y = min(min_y, s_y, b_y)
        # if min_coordinates <= s_x <= max_coordinates and min_coordinates <= s_y <= max_coordinates:
        sensors.append((s_x, s_y))
        if min_coordinates <= b_x <= max_coordinates and min_coordinates <= b_y <= max_coordinates:
            beacons.append((b_x, b_y))

    result_positions = []
    visited_positions = []
    temp = set()
    beacons_on_target_count = 0
    beacons_on_target = []
    for s, b in zip(sensors, beacons):
        if b[1] == target_y and b not in beacons_on_target:
            beacons_on_target_count += 1
            beacons_on_target.append(b)
        y_path = abs(s[1] - b[1])
        x_path = abs(s[0] - b[0])
        path = x_path + y_path
        if path >= abs(s[1] - target_y):
            y_steps = abs(target_y - s[1])
            x_steps = path - y_steps
            temp.add((s[0], x_steps))
            # for step in range(x_steps+1):
            #     if (s[0] + step, target_y) not in beacons and (s[0] + step, target_y) not in visited_positions:
            #         visited_positions.append((s[0] + step, target_y))
            #     if (s[0] - step, target_y) not in beacons and (s[0] - step, target_y) not in visited_positions:
            #         visited_positions.append((s[0] - step, target_y))
        # result_positions, visited_positions = breadth_first_search(beacons, result_positions, visited_positions, s, b, 10)
        # result_positions, visited_positions = breadth_first_search(beacons, result_positions, visited_positions, s, b, 2000000)

    right_position = None
    left_position = None
    for pos, steps in temp:
        if right_position is None or pos + steps > right_position:
            right_position = pos + steps
        if left_position is None or pos - steps < left_position:
            left_position = pos - steps

    return right_position + abs(left_position) - beacons_on_target_count + 1

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        _input = prepare_input(f)

    _input_copy = copy.deepcopy(_input)
    # answer1 = part_one(_input_copy)
    # print("Part one:")
    # print("Answer: {}".format(answer1))
    # print()
    answer2 = part_two(_input)
    print("Part two:")
    print("Answer: {}".format(answer2))
