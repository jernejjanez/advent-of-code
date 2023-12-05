import copy


def prepare_input(file):
    cards = {}
    for line in file:
        line = line[5:].strip()
        card_id, numbers = line.split(": ")
        winning_numbers, my_numbers = numbers.split(" | ")
        winning_numbers = winning_numbers.strip().split()
        my_numbers = my_numbers.strip().split()
        cards[card_id] = (winning_numbers, my_numbers)
    return cards


def part_one(_input):
    _sum = 0
    for card_id, numbers in _input.items():
        matches = -1
        winning_numbers, my_numbers = numbers
        for number in my_numbers:
            if number in winning_numbers:
                matches += 1
        if matches != -1:
            _sum += 2 ** matches
    return _sum


def part_two(_input):
    number_of_extra_cards = 0
    cards_copies = {}
    for card_id, numbers in _input.items():
        winning_numbers, my_numbers = numbers
        extra_copies = 0
        next_copy = int(card_id) + 1
        if card_id in cards_copies:
            extra_copies = cards_copies[card_id]
        for number in my_numbers:
            if number in winning_numbers:
                if str(next_copy) in cards_copies:
                    cards_copies[str(next_copy)] += (1 + extra_copies)
                else:
                    cards_copies[str(next_copy)] = 1 + extra_copies
                next_copy += 1
    for _, val in cards_copies.items():
        number_of_extra_cards += val
    return len(_input) + number_of_extra_cards


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
