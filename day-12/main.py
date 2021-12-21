def prepare_input(file):
    caves = {}
    for line in file:
        first_cave, second_cave = line.strip().split("-")
        if second_cave != "start" and first_cave != "end":
            if first_cave not in caves:
                caves[first_cave] = [second_cave]
            else:
                caves[first_cave].append(second_cave)
        if second_cave != "end" and first_cave != "start":
            if second_cave not in caves:
                caves[second_cave] = [first_cave]
            else:
                caves[second_cave].append(first_cave)

    return caves


def find_all_paths_part_one(caves_dict, current_cave, end_cave, path):
    path = path + [current_cave]

    if current_cave == end_cave:
        return [path]
    if current_cave not in caves_dict:
        return []

    paths = []
    for next_cave in caves_dict[current_cave]:
        if next_cave not in path or next_cave.isupper():
            new_paths = find_all_paths_part_one(caves_dict, next_cave, end_cave, path)
            for new_path in new_paths:
                paths.append(new_path)

    return paths


def part_one(_input):
    return len(find_all_paths_part_one(_input, "start", "end", []))


def find_all_paths_part_two(caves_dict, current_cave, end_cave, path, small_cave_visited_twice):
    path = path + [current_cave]

    if current_cave == end_cave:
        return [path]
    if current_cave not in caves_dict:
        return []

    paths = []
    for next_cave in caves_dict[current_cave]:
        if next_cave not in path or not small_cave_visited_twice or next_cave.isupper():
            if next_cave.isupper():
                new_paths = find_all_paths_part_two(caves_dict, next_cave, end_cave, path, small_cave_visited_twice)
            elif next_cave in path:
                new_paths = find_all_paths_part_two(caves_dict, next_cave, end_cave, path, True)
            else:
                new_paths = find_all_paths_part_two(caves_dict, next_cave, end_cave, path, small_cave_visited_twice)
            for new_path in new_paths:
                paths.append(new_path)

    return paths


def part_two(_input):
    return len(find_all_paths_part_two(_input, "start", "end", [], False))


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
