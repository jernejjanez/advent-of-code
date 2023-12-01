import copy
import sys


def prepare_input(file):
    return [line.strip() for line in file]


def part_one(_input):
    _sum = 0

    for line in _input:
        first_digit = None
        last_digit = None
        for c in line:
            if c.isdigit() and first_digit is None:
                first_digit = c
            elif c.isdigit():
                last_digit = c

        if last_digit is None:
            last_digit = first_digit

        _sum += int(first_digit + last_digit)

    return _sum


def part_two(_input):
    _sum = 0

    number_strings = {
        "1": "one",
        "2": "two",
        "3": "three",
        "4": "four",
        "5": "five",
        "6": "six",
        "7": "seven",
        "8": "eight",
        "9": "nine"
    }

    for line in _input:
        first_integer_digit = None
        first_integer_digit_index = None
        last_integer_digit = None
        last_integer_digit_index = None
        for i, c in enumerate(line):
            if c.isdigit() and first_integer_digit is None:
                first_integer_digit = c
                first_integer_digit_index = i
            elif c.isdigit():
                last_integer_digit = c
                last_integer_digit_index = i

        if last_integer_digit is None:
            last_integer_digit = first_integer_digit
            last_integer_digit_index = first_integer_digit_index

        first_string_digit = None
        first_string_digit_index = sys.maxsize
        last_string_digit = None
        last_string_digit_index = -sys.maxsize
        for key, val in number_strings.items():
            first_occurrence = line.find(val)
            last_occurrence = line.rfind(val)
            if first_occurrence != -1 and first_occurrence < first_string_digit_index:
                first_string_digit_index = first_occurrence
                first_string_digit = key
            if last_occurrence != -1 and last_occurrence > last_string_digit_index:
                last_string_digit_index = last_occurrence
                last_string_digit = key

        if last_string_digit is None:
            last_string_digit = first_string_digit
            last_string_digit_index = first_string_digit_index

        first_digit = -1
        last_digit = -1
        if first_integer_digit is not None and first_string_digit is not None:
            first_digit = first_integer_digit if first_integer_digit_index < first_string_digit_index else first_string_digit
        elif first_integer_digit is not None:
            first_digit = first_integer_digit
        elif first_string_digit is not None:
            first_digit = first_string_digit

        if last_integer_digit is not None and last_string_digit is not None:
            last_digit = last_integer_digit if last_integer_digit_index > last_string_digit_index else last_string_digit
        elif last_integer_digit is not None:
            last_digit = last_integer_digit
        elif last_string_digit is not None:
            last_digit = last_string_digit

        _sum += int(first_digit + last_digit)

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
