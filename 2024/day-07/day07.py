import copy
from itertools import product


def prepare_input(file):
    equations = []
    for line in file:
        equation = line.strip().split(":")
        equations.append((int(equation[0]), list(map(int, equation[1].split()))))
    return equations


def part_one(_input):
    _sum = 0
    for equation in _input:
        test_value, numbers = equation
        operators_list = list(product("+*", repeat=len(numbers) - 1))
        for operators in operators_list:
            numbers_copy = copy.deepcopy(numbers)
            for i, operator in enumerate(operators):
                if operator == "+":
                    calculated_value = numbers_copy[0] + numbers_copy[1]
                elif operator == "*":
                    calculated_value = numbers_copy[0] * numbers_copy[1]
                numbers_copy = numbers_copy[2:]
                numbers_copy.insert(0, calculated_value)
            if numbers_copy[0] == test_value:
                _sum += test_value
                break
    return _sum


def only_sum_and_mult(_input):
    _sum = 0
    already_validated = []
    for equation in _input:
        test_value, numbers = equation
        operators_list = list(product("+*", repeat=len(numbers) - 1))
        for operators in operators_list:
            numbers_copy = copy.deepcopy(numbers)
            for i, operator in enumerate(operators):
                if operator == "+":
                    calculated_value = numbers_copy[0] + numbers_copy[1]
                elif operator == "*":
                    calculated_value = numbers_copy[0] * numbers_copy[1]
                numbers_copy = numbers_copy[2:]
                numbers_copy.insert(0, calculated_value)
            if numbers_copy[0] == test_value:
                _sum += test_value
                already_validated.append(test_value)
                break
    return _sum, already_validated


def part_two(_input):
    _sum, already_validated = only_sum_and_mult(_input)
    for equation in _input:
        test_value, numbers = equation
        if test_value not in already_validated:
            operators_list = list(product("+*|", repeat=len(numbers) - 1))
            for operators in operators_list:
                numbers_copy = copy.deepcopy(numbers)
                for i, operator in enumerate(operators):
                    if operator == "+":
                        calculated_value = numbers_copy[0] + numbers_copy[1]
                    elif operator == "*":
                        calculated_value = numbers_copy[0] * numbers_copy[1]
                    elif operator == "|":
                        calculated_value = int(str(numbers_copy[0]) + str(numbers_copy[1]))
                    numbers_copy = numbers_copy[2:]
                    numbers_copy.insert(0, calculated_value)
                if numbers_copy[0] == test_value:
                    _sum += test_value
                    break
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
