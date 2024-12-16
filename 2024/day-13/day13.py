import copy

def prepare_input(file):
    claws = []
    i = 0
    for line in file:
        if line == "\n":
            i = 0
            continue
        if i == 0:
            a_x, a_y = line.split("Button A: ")[1].split(",")
            a_x = int(a_x.split("+")[1])
            a_y = int(a_y.split("+")[1])

        elif i == 1:
            b_x, b_y = line.split("Button B: ")[1].split(",")
            b_x = int(b_x.split("+")[1])
            b_y = int(b_y.split("+")[1])
        else:
            prize_x, prize_y = line.split("Prize: ")[1].split(",")
            prize_x = int(prize_x.split("=")[1])
            prize_y = int(prize_y.split("=")[1])
            claws.append(((a_x, a_y), (b_x, b_y), (prize_x, prize_y)))
        i += 1
    return claws

def part_one(_input):
    _sum = 0
    for button_a, button_b, prize in _input:
        for i in range(100):
            for j in range(100):
                if i * button_a[0] + j * button_b[0] == prize[0] and i * button_a[1] + j * button_b[1] == prize[1]:
                    _sum += i * 3 + j
    return _sum

def part_two(_input):
    _sum = 0
    for button_a, button_b, prize in _input:
        for i in range(100):
            for j in range(100):
                if i * button_a[0] + j * button_b[0] == prize[0] and i * button_a[1] + j * button_b[1] == prize[1]:
                    _sum += i * 3 + j
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
