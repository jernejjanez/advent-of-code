import copy
import ast

def prepare_input(file):
    return [ast.literal_eval(line.strip()) for line in file if line != "\n"]

def is_order_correct(list1, list2):
    for i in range(max(len(list1), len(list2))):
        v1 = list1[i] if len(list1) != i else None
        v2 = list2[i] if len(list2) != i else None
        if v1 is None:
            return True
        elif v2 is None:
            return False
        elif type(v1) is list and type(v2) is list:
            is_correct = is_order_correct(v1, v2)
            if is_correct is not None:
                return is_correct
        elif type(v1) is list and type(v2) is int:
            is_correct = is_order_correct(v1, [v2])
            if is_correct is not None:
                return is_correct
        elif type(v1) is int and type(v2) is list:
            is_correct = is_order_correct([v1], v2)
            if is_correct is not None:
                return is_correct
        elif type(v1) is int and type(v2) is int:
            if v1 < v2:
                return True
            elif v1 > v2:
                return False
            elif v1 == v2:
                continue

def part_one(_input):
    result = []
    idx = 0
    while len(_input) != 0:
        idx += 1
        list1 = _input.pop(0)
        list2 = _input.pop(0)
        if is_order_correct(list1, list2):
            result.append(idx)

    return sum(result)

def part_two(_input):
    _input.append([[2]])
    _input.append([[6]])
    correct_order = [_input.pop(0)]
    result = 1
    while len(_input) != 0:
        _list = _input.pop(0)
        idx = 0
        for i in range(len(correct_order)):
            if is_order_correct(correct_order[i], _list):
                idx += 1
            else:
                break
        correct_order.insert(idx, _list)
        if _list == [[2]] or _list == [[6]]:
            result *= idx + 1

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
