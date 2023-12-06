import copy
import math


def prepare_input(file):
    times = []
    distances = []
    for i, line in enumerate(file):
        line = line.strip()
        if i == 0:
            times = line[5:].split()
        elif i == 1:
            distances = line[9:].split()
    return times, distances


def find_lower_cutoff(time, distance):
    for hold_button in range(0, time):
        traveled = (time - hold_button) * hold_button
        if traveled > distance:
            return hold_button
    return -1


def find_upper_cutoff(time, distance):
    for hold_button in range(time, 0, -1):
        traveled = (time - hold_button) * hold_button
        if traveled > distance:
            return hold_button
    return -1


def part_one(_input):
    result = []
    times, distances = _input
    for time, distance in zip(times, distances):
        lower_cutoff = find_lower_cutoff(int(time), int(distance))
        upper_cutoff = find_upper_cutoff(int(time), int(distance))
        result.append(upper_cutoff - lower_cutoff + 1)
    return math.prod(result)


def part_two(_input):
    times, distances = _input
    final_race_time = ""
    final_race_distance = ""
    for time, distance in zip(times, distances):
        final_race_time += time
        final_race_distance += distance
    lower_cutoff = find_lower_cutoff(int(final_race_time), int(final_race_distance))
    upper_cutoff = find_upper_cutoff(int(final_race_time), int(final_race_distance))
    return upper_cutoff - lower_cutoff + 1


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
