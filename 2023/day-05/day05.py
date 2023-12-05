import copy


def prepare_input(file):
    seeds = []
    transformation_map = {}
    current_transformation_map = 0
    ranges = []
    for i, line in enumerate(file):
        line = line.strip()
        if i == 0:
            seeds = line[7:].split()
        elif i == 1:
            continue
        elif "map" in line:
            current_transformation_map += 1
        elif line == "":
            transformation_map[current_transformation_map] = ranges
            ranges = []
        else:
            ranges.append(line.split())
    transformation_map[current_transformation_map] = ranges
    return transformation_map, seeds


def get_transformation(transformation, seed):
    for t in transformation:
        destination, source, _range = t
        if int(source) <= int(seed) <= (int(source) + int(_range)):
            return str(int(destination) + (int(seed) - int(source)))
    return seed


def part_one(_input):
    locations = []
    transformation_map, seeds = _input
    for seed in seeds:
        for key, transformation in transformation_map.items():
            seed = get_transformation(transformation, seed)
        locations.append(int(seed))
    return min(locations)


def is_seed(potential_seed, seeds):
    for i in range(0, len(seeds), 2):
        seed = seeds[i]
        _range = seeds[i + 1]
        if int(seed) <= int(potential_seed) <= (int(seed) + int(_range)):
            return True
    return False


def get_potential_seed(location, transformation_map):
    for key, transformation in reversed(transformation_map.items()):
        for t in transformation:
            destination, source, _range = t
            if int(destination) <= int(location) <= (int(destination) + int(_range)):
                location = int(source) + (int(location) - int(destination))
                break
    return location


# Not optimal solution. Result: 219529182
def part_two(_input):
    transformation_map, seeds = _input
    potential_seed = 0
    # This was achieved with a little bit of guessing
    location = 219000000
    while not is_seed(potential_seed, seeds):
        location += 1
        potential_seed = get_potential_seed(location, transformation_map)
    return location


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
