import copy

path = []

def prepare_input(file):
    _dict = {}
    for line in file:
        monkey_name, job = line.split(":")
        try:
            job = int(job.strip())
        except:
            job = job.strip()
        _dict[monkey_name] = job
    return _dict

def get_result(_dict, name):
    if type(_dict[name]) == int:
        return _dict[name]
    else:
        p1 = _dict[name][0:4]
        p2 = _dict[name][7:11]
        operator = _dict[name][5]
        if operator == "+":
            return get_result(_dict, p1) + get_result(_dict, p2)
        elif operator == "-":
            return get_result(_dict, p1) - get_result(_dict, p2)
        if operator == "*":
            return get_result(_dict, p1) * get_result(_dict, p2)
        if operator == "/":
            return get_result(_dict, p1) / get_result(_dict, p2)

def uses_monkey(_dict, name, monkey):
    global path
    if type(_dict[name]) == int:
        if name == monkey:
            return True
        else:
            return False
    else:
        p1 = _dict[name][0:4]
        p2 = _dict[name][7:11]
        p1_uses = uses_monkey(_dict, p1, monkey)
        # p2_uses = uses_monkey(_dict, p2, monkey)
        if p1_uses:
            path.append(p1)
            return uses_monkey(_dict, p1, monkey)
        else:
            path.append(p2)
            return uses_monkey(_dict, p2, monkey)


def part_one(_input):
    return int(get_result(_input, "root"))

def find_monkey(_dict, path, current, monkey):
    if type(_dict[current]) == int:
        if current == monkey:
            return path
        return
    else:
        p1 = _dict[current][0:4]
        p2 = _dict[current][7:11]
        operator = _dict[current][5]
        path.append(find_monkey(_dict, path, p1, monkey))
        path.append(find_monkey(_dict, path, p2, monkey))

def part_two(_input):
    # path = find_monkey(_input, [], "root", "humn")
    uses_monkey(_input, "root", "humn")
    p1 = _input["root"][0:4]
    p2 = _input["root"][7:11]
    p1_uses = uses_monkey(_input, p1, "humn")
    p2_uses = uses_monkey(_input, p2, "humn")
    p1_result = int(get_result(_input, p1))
    p2_result = int(get_result(_input, p2))
    print(p2_result)
    value = 1
    while p1_result != p2_result:
        if p1_result > p2_result:
            value *= 2
        else:
            value /= 1.5
        if value % 10000 == 0:
            print(p1_result)
        _input["humn"] = int(value)
        p1_result = int(get_result(_input, p1))

    return value

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
