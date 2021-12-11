def part_one(horizontal_positions):
    optimal_positions = max(horizontal_positions)
    optimal_fuel = 100000000
    current_fuel = 100000000
    for optimal_position in range(optimal_positions):
        if current_fuel < optimal_fuel:
            optimal_fuel = current_fuel
        current_fuel = 0
        for horizontal_position in horizontal_positions:
            current_fuel += abs(horizontal_position - optimal_position)

    return optimal_fuel


def part_two(horizontal_positions):
    optimal_positions = max(horizontal_positions)
    optimal_fuel = 100000000
    current_fuel = 100000000
    for optimal_position in range(optimal_positions):
        if current_fuel < optimal_fuel:
            optimal_fuel = current_fuel
        current_fuel = 0
        for horizontal_position in horizontal_positions:
            distance = abs(horizontal_position - optimal_position)
            for move in range(1, distance + 1):
                current_fuel += move

    return optimal_fuel


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        _input = [list(map(int, list(line.strip().split(",")))) for line in f][0]

    answer1 = part_one(_input)
    print("Part one:")
    print("Answer: {}".format(int(answer1)))
    print()
    answer2 = part_two(_input)
    print("Part two:")
    print("Answer: {}".format(answer2))
