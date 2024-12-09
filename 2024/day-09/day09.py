import copy


def prepare_input(file):
    return [list(map(int, line.strip())) for line in file][0]


def part_one(_input):
    disk_map = []
    _id = 0
    for i, block in enumerate(_input):
        if block == 0:
            continue
        if i % 2 == 0:
            disk_map.append((_id, block))
            _id += 1
        else:
            disk_map.append((None, block))

    is_done = False
    idx = 0
    while idx < len(disk_map) and not is_done:
        block, how_many = disk_map.pop()
        if block is None:
            continue
        while how_many != 0:
            if idx == len(disk_map):
                disk_map.append((block, how_many))
                how_many -= how_many
                is_done = True
                break
            current_block, spaces = disk_map[idx]
            if current_block is not None:
                idx += 1
                continue
            if spaces > how_many:
                disk_map[idx] = (None, spaces-how_many)
                disk_map.insert(idx, (block, how_many))
                how_many -= how_many
            elif spaces < how_many:
                disk_map[idx] = (block, spaces)
                how_many -= spaces
            elif spaces == how_many:
                disk_map[idx] = (block, spaces)
                how_many -= spaces

    _sum = 0
    idx = 0
    for sections in disk_map:
        block, length = sections
        for _ in range(length):
            _sum += block * idx
            idx += 1

    return _sum


def part_two(_input):
    disk_map = []
    _id = 0
    for i, block in enumerate(_input):
        if block == 0:
            continue
        if i % 2 == 0:
            disk_map.append((_id, block))
            _id += 1
        else:
            disk_map.append((None, block))

    idx = 0
    take_id = len(disk_map)-1
    while take_id != 0:
        block, how_many = disk_map[take_id]
        if block is None:
            take_id -= 1
            continue

        while True:
            if take_id == idx:
                take_id -= 1
                break

            current_block, spaces = disk_map[idx]

            if current_block is not None:
                idx += 1
                continue

            if spaces > how_many:
                disk_map[take_id] = (None, how_many)
                disk_map[idx] = (None, spaces - how_many)
                disk_map.insert(idx, (block, how_many))
                break
            elif spaces < how_many:
                idx += 1
                continue
            elif spaces == how_many:
                disk_map[take_id] = (None, how_many)
                disk_map[idx] = (block, how_many)
                break
        idx = 0

    _sum = 0
    idx = 0
    for sections in disk_map:
        block, length = sections
        if block is not None:
            for _ in range(length):
                _sum += block * idx
                idx += 1
        else:
            idx += length

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
