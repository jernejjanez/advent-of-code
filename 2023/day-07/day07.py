import copy


def prepare_input(file):
    hands = []
    for line in file:
        hand, bid = line.strip().split()
        hands.append((hand, int(bid)))
    return hands


def get_hand_strength(hand):
    seen_cards = []
    three_of_a_kind = False
    pair = False
    for card in hand:
        if card in seen_cards:
            continue
        number_of_cards = hand.count(card)
        if number_of_cards == 5:
            return 7
        if number_of_cards == 4:
            return 6
        if number_of_cards == 3:
            seen_cards.append(card)
            if pair:
                return 5
            else:
                three_of_a_kind = True
        if number_of_cards == 2:
            seen_cards.append(card)
            if three_of_a_kind:
                return 5
            elif pair:
                return 3
            else:
                pair = True
    if three_of_a_kind:
        return 4
    if pair:
        return 2
    return 1


def is_stronger(new_hand, hand, card_order):
    for position in range(0, len(new_hand)):
        if card_order.index(new_hand[position]) < card_order.index(hand[position]):
            return True
        elif card_order.index(new_hand[position]) == card_order.index(hand[position]):
            continue
        else:
            return False


def insert_hand(hands, new_hand, new_bid, card_order):
    if hands:
        for i, (hand, bid) in enumerate(hands):
            if is_stronger(new_hand, hand, card_order):
                if i == len(hands) - 1:
                    hands.append((new_hand, new_bid))
                    break
                else:
                    continue
            else:
                hands.insert(i, (new_hand, new_bid))
                break
    else:
        hands.append((new_hand, new_bid))
    return hands


def part_one(_input):
    sorted_hands = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: []}
    for hand, bid in _input:
        hand_strength = get_hand_strength(hand)
        sorted_hands[hand_strength] = insert_hand(sorted_hands[hand_strength], hand, bid,
                                                  ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"])
    rank = 1
    total_winnings = 0
    for _, hands in sorted_hands.items():
        for hand, bid in hands:
            total_winnings += (bid * rank)
            rank += 1
    return total_winnings


def get_hand_strength_jokers(hand):
    seen_cards = ["J"]
    three_of_a_kind = False
    pair = False
    number_of_jokers = hand.count("J")
    used_joker = False
    if number_of_jokers == 5:
        return 7
    for card in hand:
        if card in seen_cards:
            continue
        number_of_cards = hand.count(card)
        if number_of_cards == 5:
            return 7
        elif number_of_cards == 4:
            if number_of_jokers == 1:
                return 7
            return 6
        elif number_of_cards == 3:
            seen_cards.append(card)
            if not used_joker:
                if number_of_jokers == 2:
                    return 7
                elif number_of_jokers == 1:
                    return 6
            if pair:
                return 5
            else:
                three_of_a_kind = True
        elif number_of_cards == 2:
            seen_cards.append(card)
            if not used_joker:
                if number_of_jokers == 3:
                    return 7
                elif number_of_jokers == 2:
                    return 6
                elif number_of_jokers == 1:
                    if pair:
                        return 5
                    else:
                        three_of_a_kind = True
                        used_joker = True
                        continue
            if three_of_a_kind:
                return 5
            elif pair:
                return 3
            else:
                pair = True
    if three_of_a_kind:
        return 4
    if pair:
        return 2
    if number_of_jokers == 4:
        return 7
    elif number_of_jokers == 3:
        return 6
    elif number_of_jokers == 2:
        return 4
    elif number_of_jokers == 1:
        return 2
    return 1


def part_two(_input):
    sorted_hands = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: []}
    for hand, bid in _input:
        hand_strength = get_hand_strength_jokers(hand)
        sorted_hands[hand_strength] = insert_hand(sorted_hands[hand_strength], hand, bid,
                                                  ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"])
    rank = 1
    total_winnings = 0
    for _, hands in sorted_hands.items():
        for hand, bid in hands:
            total_winnings += (bid * rank)
            rank += 1
    return total_winnings


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
