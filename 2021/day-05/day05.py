def prepare_coordinates(file):
    _coordinates = []
    for line in file:
        x1y1, x2y2 = line.strip().split("->")
        x1, y1 = map(int, x1y1.split(","))
        x2, y2 = map(int, x2y2.split(","))
        _coordinates.append({"x1": x1, "y1": y1, "x2": x2, "y2": y2})

    return _coordinates


def count_overlaps(_map):
    count = 0
    for key, value in _map.items():
        if value > 1:
            count += 1

    return count


def part_one(_coordinates):
    _map = {}
    for coordinate in _coordinates:
        if coordinate["x1"] == coordinate["x2"]:
            if coordinate["y1"] < coordinate["y2"]:
                y_range = [*range(coordinate["y1"], coordinate["y2"] + 1, 1)]
            else:
                y_range = [*range(coordinate["y1"], coordinate["y2"] - 1, -1)]
            for y in y_range:
                if str(coordinate["x1"]) + "," + str(y) in _map:
                    _map[str(coordinate["x1"]) + "," + str(y)] += 1
                else:
                    _map[str(coordinate["x1"]) + "," + str(y)] = 1
        elif coordinate["y1"] == coordinate["y2"]:
            if coordinate["x1"] < coordinate["x2"]:
                x_range = [*range(coordinate["x1"], coordinate["x2"] + 1, 1)]
            else:
                x_range = [*range(coordinate["x1"], coordinate["x2"] - 1, -1)]
            for x in x_range:
                if str(x) + "," + str(coordinate["y1"]) in _map:
                    _map[str(x) + "," + str(coordinate["y1"])] += 1
                else:
                    _map[str(x) + "," + str(coordinate["y1"])] = 1

    return _map


def part_two(_coordinates):
    _map = part_one(_coordinates)
    for coordinate in _coordinates:
        x_range = []
        y_range = []
        if coordinate["x1"] < coordinate["x2"] and coordinate["y1"] < coordinate["y2"]:
            x_range = [*range(coordinate["x1"], coordinate["x2"] + 1, 1)]
            y_range = [*range(coordinate["y1"], coordinate["y2"] + 1, 1)]
        elif coordinate["x1"] < coordinate["x2"] and coordinate["y1"] > coordinate["y2"]:
            x_range = [*range(coordinate["x1"], coordinate["x2"] + 1, 1)]
            y_range = [*range(coordinate["y1"], coordinate["y2"] - 1, -1)]
        elif coordinate["x1"] > coordinate["x2"] and coordinate["y1"] < coordinate["y2"]:
            x_range = [*range(coordinate["x1"], coordinate["x2"] - 1, -1)]
            y_range = [*range(coordinate["y1"], coordinate["y2"] + 1, 1)]
        elif coordinate["x1"] > coordinate["x2"] and coordinate["y1"] > coordinate["y2"]:
            x_range = [*range(coordinate["x1"], coordinate["x2"] - 1, -1)]
            y_range = [*range(coordinate["y1"], coordinate["y2"] - 1, -1)]
        for x, y in zip(x_range, y_range):
            if str(x) + "," + str(y) in _map:
                _map[str(x) + "," + str(y)] += 1
            else:
                _map[str(x) + "," + str(y)] = 1

    return _map


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        coordinates = prepare_coordinates(f)

    map1 = part_one(coordinates)
    print("Part one:")
    print("Answer: {}".format(count_overlaps(map1)))
    print()
    map2 = part_two(coordinates)
    print("Part two:")
    print("Answer: {}".format(count_overlaps(map2)))
