def part_one(depths):
    increases = 0
    decreases = 0
    previous_depth = None

    for depth in depths:
        current_depth = depth
        if previous_depth is not None:
            if current_depth > previous_depth:
                increases += 1
            else:
                decreases += 1
        previous_depth = current_depth

    print("Increases: {}".format(increases))
    print("Decreases: {}".format(decreases))


def part_two(depths):
    sliding_window = 3
    three_measurement_depths = []

    for i in range(len(depths) - sliding_window + 1):
        three_measurement_depths.append(sum(depths[i: i + sliding_window]))

    return three_measurement_depths


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        lines = [int(line) for line in file]

    print("Part one:")
    part_one(lines)
    print()
    print("Part two:")
    three_measure_depths = part_two(lines)
    part_one(three_measure_depths)
