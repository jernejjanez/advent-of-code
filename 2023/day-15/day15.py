import copy
from collections import OrderedDict


def prepare_input(file):
    sequence = []
    for line in file:
        sequence = line.strip().split(",")
    return sequence


def do_procedure(char, current_value):
    current_value += ord(char)
    current_value *= 17
    current_value %= 256
    return current_value


def hash_algorithm(word):
    current_value = 0
    for c in word:
        current_value = do_procedure(c, current_value)
    return current_value


def part_one(_input):
    _sum = 0
    for step in _input:
        _sum += hash_algorithm(step)
    return _sum


def add_box(boxes, label, label_number, focal_length):
    if label_number not in boxes:
        boxes[label_number] = OrderedDict({label: focal_length})
    else:
        boxes[label_number][label] = focal_length
    return boxes


def remove_box(boxes, label, label_number):
    if label_number not in boxes:
        return boxes
    else:
        if label in boxes[label_number]:
            del boxes[label_number][label]
    return boxes


def calculate_focusing_power(boxes):
    _sum = 0
    for box_number, slots in boxes.items():
        for i, (_, value) in enumerate(slots.items()):
            _sum += (box_number + 1) * (i + 1) * value
    return _sum


def part_two(_input):
    boxes = {}
    for step in _input:
        if "=" in step:
            label, focal_length = step.split("=")
            label_number = hash_algorithm(label)
            boxes = add_box(boxes, label, label_number, int(focal_length))
        elif "-" in step:
            label, _ = step.split("-")
            label_number = hash_algorithm(label)
            boxes = remove_box(boxes, label, label_number)
    return calculate_focusing_power(boxes)


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
