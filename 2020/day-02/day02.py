def prepare_input(file):
    return [line.strip().split() for line in file]


def part_one(_input):
    number_of_valid_passwords = 0
    for occurrences, char, password in _input:
        lowest, highest = occurrences.split("-")
        count = password.count(char[0])
        if int(lowest) <= count <= int(highest):
            number_of_valid_passwords += 1

    return number_of_valid_passwords


def part_two(_input):
    number_of_valid_passwords = 0
    for occurrences, char, password in _input:
        first_index, second_index = occurrences.split("-")
        if password[int(first_index)-1] == char[0] and password[int(second_index)-1] != char[0] \
                or password[int(first_index)-1] != char[0] and password[int(second_index)-1] == char[0]:
            number_of_valid_passwords += 1

    return number_of_valid_passwords


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
