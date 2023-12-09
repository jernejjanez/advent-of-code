import copy


def prepare_input(file):
    values = []
    for line in file:
        values.append(list(map(int, line.strip().split())))
    return values


def calculate_next_step(last_steps):
    next_step = 0
    for step in reversed(last_steps):
        next_step += step
    return next_step


def are_all_zero(steps):
    return all(step == 0 for step in steps)


def part_one(_input):
    _sum = 0
    for value in _input:
        last_steps = []
        step = value
        while not are_all_zero(step):
            value = step
            step = []
            for i in range(len(value)):
                if i == len(value) - 1:
                    last_steps.append(value[i])
                else:
                    step.append(value[i + 1] - value[i])
        _sum += calculate_next_step(last_steps)
    return _sum


def calculate_previous_step(last_steps):
    previous_step = 0
    for step in reversed(last_steps):
        previous_step = step - previous_step
    return previous_step


def part_two(_input):
    _sum = 0
    for value in _input:
        first_steps = []
        step = value
        while not are_all_zero(step):
            value = step
            step = []
            for i in range(len(value)):
                if i == 0:
                    first_steps.append(value[i])
                if i == len(value) - 1:
                    continue
                else:
                    step.append(value[i + 1] - value[i])
        _sum += calculate_previous_step(first_steps)
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
