import copy

def get_operation_function(operation_items):
    if operation_items[2] == "old":
        if operation_items[1] == "+":
            return lambda old : old + old
        else:
            return lambda old : old * old
    else:
        if operation_items[1] == "+":
            return lambda old : old + int(operation_items[2])
        else:
            return lambda old : old * int(operation_items[2])

def get_test_function(divisor):
    return lambda value : True if value % divisor == 0 else False

def prepare_input(file):
    _dict = {}
    idx = 0
    curr_monkey = -1
    for line in file:
        if idx == 0:
            curr_monkey = int(line.split()[1][0])
            _dict[curr_monkey] = {}
        elif idx == 1:
            items = list(map(int, line.strip().split("Starting items:")[1].strip().split(", ")))
            _dict[curr_monkey]["items"] = items
        elif idx == 2:
            operation_items = line.strip().split("Operation: new =")[1].strip().split()
            _dict[curr_monkey]["operation"] = get_operation_function(operation_items)
        elif idx == 3:
            divisor = int(line.strip().split()[-1])
            _dict[curr_monkey]["divisor"] = divisor
            _dict[curr_monkey]["test"] = get_test_function(divisor)
        elif idx == 4:
            true = int(line.strip().split()[-1])
            _dict[curr_monkey]["true"] = true
        elif idx == 5:
            false = int(line.strip().split()[-1])
            _dict[curr_monkey]["false"] = false
        idx += 1
        if line == "\n":
            idx = 0
    return _dict

def lower_worry_level(level):
    return int(level / 3)

def part_one(_input):
    result = {}
    for _ in range(20):
        for key, val in _input.items():
            while len(val["items"]) > 0:
                item = val["items"].pop(0)
                if key not in result:
                    result[key] = 1
                else:
                    result[key] += 1
                item = val["operation"](item)
                item = lower_worry_level(item)
                if val["test"](item):
                    _input[val["true"]]["items"].append(item)
                else:
                    _input[val["false"]]["items"].append(item)

    result = dict(sorted(result.items(), key=lambda _item: _item[1]))
    _max = list(result)[-1]
    second_max = list(result)[-2]

    return result[_max] * result[second_max]

def group_mod(_input):
    mod = 1
    for val in _input.values():
        mod *= val["divisor"]
    return mod

def part_two(_input):
    result = {}
    mod = group_mod(_input)
    for i in range(10000):
        for key, val in _input.items():
            val["items"].reverse()
            while len(val["items"]) > 0:
                item = val["items"].pop()
                result[key] = 1 if key not in result else result[key] + 1
                item = val["operation"](item)
                item %= mod
                if val["test"](item):
                    _input[val["true"]]["items"].append(item)
                else:
                    _input[val["false"]]["items"].append(item)

    result = dict(sorted(result.items(), key=lambda _item: _item[1]))
    _max = list(result)[-1]
    second_max = list(result)[-2]

    return result[_max] * result[second_max]

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
