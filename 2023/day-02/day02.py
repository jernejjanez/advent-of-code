import copy


def prepare_input(file):
    games = {}
    for line in file:
        line = line.strip()
        game_id, subsets_of_cubes = line.split(": ")
        game_id = game_id.split()[1]
        subsets_of_cubes = subsets_of_cubes.split("; ")
        games[game_id] = subsets_of_cubes
    return games


def is_draw_possible(drawn_cubes, max_red, max_green, max_blue):
    for cubes in drawn_cubes:
        number, color = cubes.split()
        if color == "red" and int(number) > max_red:
            return False
        if color == "green" and int(number) > max_green:
            return False
        if color == "blue" and int(number) > max_blue:
            return False
    return True


def is_valid_game(subsets_of_cubes, max_red, max_green, max_blue):
    for subset in subsets_of_cubes:
        if not is_draw_possible(subset.split(", "), max_red, max_green, max_blue):
            return False
    return True


def part_one(_input, max_red=12, max_green=13, max_blue=14):
    _sum = 0
    for game_id, subsets_of_cubes in _input.items():
        if is_valid_game(subsets_of_cubes, max_red, max_green, max_blue):
            _sum += int(game_id)
    return _sum


def drawn_colors(drawn_cubes):
    number_of_red_cubes = 0
    number_of_green_cubes = 0
    number_of_blue_cubes = 0
    for cube in drawn_cubes:
        number, color = cube.split()
        if color == "red":
            number_of_red_cubes = int(number)
        if color == "green":
            number_of_green_cubes = int(number)
        if color == "blue":
            number_of_blue_cubes = int(number)
    return number_of_red_cubes, number_of_green_cubes, number_of_blue_cubes


def part_two(_input):
    _sum = 0
    for game_id, subsets_of_cubes in _input.items():
        fewest_red = 0
        fewest_green = 0
        fewest_blue = 0
        for subset in subsets_of_cubes:
            red_cubes, green_cubes, blue_cubes = drawn_colors(subset.split(", "))
            if red_cubes > fewest_red:
                fewest_red = red_cubes
            if green_cubes > fewest_green:
                fewest_green = green_cubes
            if blue_cubes > fewest_blue:
                fewest_blue = blue_cubes

        _sum += (fewest_red * fewest_green * fewest_blue)
    return _sum


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
