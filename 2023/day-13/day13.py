import copy


def prepare_input(file):
    patterns = []
    current_pattern = []
    for line in file:
        line = line.strip()
        if line == "":
            patterns.append(current_pattern)
            current_pattern = []
            continue
        current_pattern.append(line)
    patterns.append(current_pattern)
    return patterns


def can_fix_smudge(line1, line2):
    for i, (c1, c2) in enumerate(zip(line1, line2)):
        if c1 != c2:
            new_line1 = line1[:i] + c2 + line1[i + 1:]
            if new_line1 == line2:
                return True
            return False
    return False


def is_reflection_possible(pattern, y1, y2, should_fix_smudge):
    smudge_fixed = False
    while 0 <= y1 and y2 < len(pattern):
        if pattern[y1] == pattern[y2]:
            y1 -= 1
            y2 += 1
        elif should_fix_smudge:
            if smudge_fixed:
                return False, False
            if can_fix_smudge(pattern[y1], pattern[y2]):
                y1 -= 1
                y2 += 1
                smudge_fixed = True
            else:
                return False, False
        else:
            return False, False
    return True, smudge_fixed


def find_reflection(pattern, multiplication, should_fix_smudge):
    reflection_possible = False
    line_of_reflection = 0
    fixed_smudge = False
    for y in range(len(pattern)):
        if y == len(pattern) - 1:
            break
        reflection_possible, fixed_smudge = is_reflection_possible(pattern, y, y + 1, should_fix_smudge)
        if should_fix_smudge and not fixed_smudge:
            continue
        if reflection_possible:
            line_of_reflection = y + 1
            break
    if should_fix_smudge:
        if reflection_possible and fixed_smudge:
            return True, multiplication * line_of_reflection
    elif reflection_possible:
        return True, multiplication * line_of_reflection
    return False, 0


def part_one(_input):
    _sum = 0
    for pattern in _input:
        has_horizontal_reflection, value = find_reflection(pattern, 100, False)
        if has_horizontal_reflection:
            _sum += value
        else:
            pattern = [''.join(list(i)[::-1]) for i in zip(*pattern)]
            has_vertical_reflection, value = find_reflection(pattern, 1, False)
            if has_vertical_reflection:
                _sum += value
    return _sum


def part_two(_input):
    _sum = 0
    for pattern in _input:
        has_horizontal_reflection, value = find_reflection(pattern, 100, True)
        if has_horizontal_reflection:
            _sum += value
        else:
            pattern = [''.join(list(i)[::-1]) for i in zip(*pattern)]
            has_vertical_reflection, value = find_reflection(pattern, 1, True)
            if has_vertical_reflection:
                _sum += value
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
