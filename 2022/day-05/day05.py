import copy


def prepare_input(file):
    _dict = {}
    instructions = []
    are_instructions = False
    for line in file:
        i = 1
        if line == "\n":
            continue
        if not are_instructions:
            if line[1] == "1":
                are_instructions = True
                continue
            for ind in range(0, len(line), 4):
                if i not in _dict:
                    _dict[i] = []
                block = line[ind:ind+3]
                if line[ind:ind+3] == "   ":
                    i += 1
                else:
                    _dict[i] += block[1]
                    i += 1
        else:
            inst = line.split()
            how_many = int(inst[1])
            _from = int(inst[3])
            _to = int(inst[5])
            instructions.append((how_many, _from, _to))

    for d in _dict.values():
        d.reverse()

    return _dict, instructions


def part_one(_input):
    _dict, instructions = _input
    for inst in instructions:
        how_many, _from, _to = inst
        for i in range(how_many):
            b = _dict[_from].pop()
            _dict[_to].append(b)

    result = ""
    for v in _dict.values():
        result += v[-1]

    return result


def part_two(_input):
    _dict, instructions = _input
    for inst in instructions:
        how_many, _from, _to = inst
        to_move = []
        for i in range(how_many):
            to_move.append(_dict[_from].pop())

        to_move.reverse()
        _dict[_to].extend(to_move)

    result = ""
    for v in _dict.values():
        result += v[-1]

    return result


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
