def prepare_input(file):
    x_area, y_area = file.read()[15:].strip().split(", y=")
    x_min, x_max = x_area.split("..")
    y_min, y_max = y_area.split("..")

    target_area = {}
    for x in range(int(x_min), int(x_max) + 1):
        for y in range(int(y_min), int(y_max) + 1):
            target_area[(x, y)] = True

    return target_area


def calculate_probe_position(_target_area, x_position, y_position, x_velocity, y_velocity, max_y):
    x_position += x_velocity
    y_position += y_velocity

    if y_position > max_y:
        max_y = y_position

    if (x_position, y_position) in _target_area:
        return max_y
    if x_position > max(_target_area)[0] or y_position < min(_target_area)[1]:
        return -1

    if x_velocity > 0:
        x_velocity -= 1
    elif x_velocity < 0:
        x_velocity += 1

    y_velocity -= 1

    return calculate_probe_position(_target_area, x_position, y_position, x_velocity, y_velocity, max_y)


def calculate_if_probe_in_target(_target_area, x_position, y_position, x_velocity, y_velocity):
    x_position += x_velocity
    y_position += y_velocity

    if (x_position, y_position) in _target_area:
        return True
    if x_position > max(_target_area)[0] or y_position < min(_target_area)[1]:
        return False

    if x_velocity > 0:
        x_velocity -= 1
    elif x_velocity < 0:
        x_velocity += 1

    y_velocity -= 1

    return calculate_if_probe_in_target(_target_area, x_position, y_position, x_velocity, y_velocity)


def part_one(target_area):
    max_y = 0
    for x_velocity in range(max(target_area)[0] + 1):
        for y_velocity in range(min(target_area)[1], max(target_area)[0] + 1):
            current_max_y = calculate_probe_position(target_area, 0, 0, x_velocity, y_velocity, 0)
            if current_max_y > max_y:
                max_y = current_max_y

    return max_y


def part_two(target_area):
    number_of_distinct_initial_velocities = 0
    for x_velocity in range(max(target_area)[0] + 1):
        for y_velocity in range(min(target_area)[1], max(target_area)[0] + 1):
            if calculate_if_probe_in_target(target_area, 0, 0, x_velocity, y_velocity):
                number_of_distinct_initial_velocities += 1

    return number_of_distinct_initial_velocities


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
