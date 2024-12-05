import copy


def prepare_input(file):
    page_ordering_rules = []
    updates = []
    first_part = True
    for line in file:
        if line == "\n":
            first_part = False
            continue
        if first_part:
            page_ordering_rules.append(tuple(map(int, line.strip().split("|"))))
        else:
            updates.append(list(map(int, line.strip().split(","))))

    return page_ordering_rules, updates


def part_one(_input):
    correct_updates = []
    page_ordering_rules, updates = _input
    for update in updates:
        correct = True
        for rule in page_ordering_rules:
            rule1, rule2 = rule
            if rule1 in update and rule2 in update:
                if update.index(rule1) >= update.index(rule2):
                    correct = False
                    break
        if correct:
            correct_updates.append(update)

    _sum = 0
    for correct_update in correct_updates:
        _sum += correct_update[len(correct_update) // 2]

    return _sum


def part_two(_input):
    incorrect_updates = []
    page_ordering_rules, updates = _input
    for update in updates:
        incorrect = False
        for rule in page_ordering_rules:
            rule1, rule2 = rule
            if rule1 in update and rule2 in update:
                idx1 = update.index(rule1)
                idx2 = update.index(rule2)
                if idx1 >= idx2:
                    incorrect = True
                    break
        if incorrect:
            incorrect_updates.append(update)

    fixed_updates = []
    while incorrect_updates:
        incorrect_update = incorrect_updates.pop()
        correct = True
        for rule in page_ordering_rules:
            rule1, rule2 = rule
            if rule1 in incorrect_update and rule2 in incorrect_update:
                idx1 = incorrect_update.index(rule1)
                idx2 = incorrect_update.index(rule2)
                if idx1 >= idx2:
                    incorrect_update[idx1], incorrect_update[idx2] = incorrect_update[idx2], incorrect_update[idx1]
                    incorrect_updates.append(incorrect_update)
                    correct = False
                    break
        if correct:
            fixed_updates.append(incorrect_update)

    _sum = 0
    for fixed_update in fixed_updates:
        _sum += fixed_update[len(fixed_update) // 2]

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
