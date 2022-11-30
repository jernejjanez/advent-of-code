from collections import Counter, defaultdict


def prepare_input(file):
    polymer_template = []
    pair_insertion_rules = {}
    polymer_template_string = ""
    lines_are_insertions = False
    n = 2
    for line in file:
        if line == "\n":
            lines_are_insertions = True
            continue
        elif lines_are_insertions:
            rule, value = line.strip().split(" -> ")
            pair_insertion_rules[rule] = value
        else:
            line = line.strip()
            polymer_template_string = line
            polymer_template = [line[i:i+n] for i in range(len(line)) if i+n <= len(line)]

    return pair_insertion_rules, polymer_template, polymer_template_string


def part_one(pair_insertion_rules_polymer_template):
    pair_insertion_rules, polymer_template, _ = pair_insertion_rules_polymer_template

    steps = 10
    n = 2
    result = ""
    for step in range(steps):
        result = ""
        for idx, polymer in enumerate(polymer_template):
            result += polymer[0] + pair_insertion_rules[polymer]
            if idx == len(polymer_template) - 1:
                result += polymer[1]

        polymer_template = [result[i:i + n] for i in range(len(result)) if i + n <= len(result)]

    result_list = [char for char in result]

    most_common_char, max_count = Counter(result_list).most_common(1)[0]
    least_common_char, min_count = Counter(result_list).most_common()[-1]

    return max_count - min_count


def transformation_step(current_dict, _pair_insertion_rules, _letter_count):
    new_dict = defaultdict(int)
    for pair, value in current_dict.items():
        insertion_letter = _pair_insertion_rules[pair]
        letters = [letter for letter in pair]
        new_dict[letters[0] + insertion_letter] += current_dict[pair]
        new_dict[insertion_letter + letters[1]] += value
        _letter_count[insertion_letter] += current_dict[pair]

    return new_dict, _letter_count


def part_two(pair_insertion_rules_polymer_template):
    pair_insertion_rules, polymer_template, polymer_template_string = pair_insertion_rules_polymer_template

    letter_count = Counter(polymer_template_string)
    polymer_template_dict = Counter(polymer_template)

    steps = 40
    for step in range(steps):
        polymer_template_dict, letter_count = transformation_step(polymer_template_dict, pair_insertion_rules, letter_count)

    max_count = max(letter_count.values())
    min_count = min(letter_count.values())

    return max_count - min_count


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        _input = prepare_input(f)

    answer1 = part_one(_input)
    print("Part one:")
    print("Answer: {}".format(int(answer1)))
    print()
    answer2 = part_two(_input)
    print("Part two:")
    print("Answer: {}".format(int(answer2)))
