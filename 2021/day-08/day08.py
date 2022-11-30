def prepare_input(file):
    signal_patterns = []
    output_values = []
    for line in file:
        signal_patterns_string, output_value_string = line.strip().split(" | ")
        signal_patterns.append(signal_patterns_string.split())
        output_values.append(output_value_string.split())

    return signal_patterns, output_values


def part_one(signal_patterns_output_value):
    signal_patterns, output_values = signal_patterns_output_value
    answer = 0
    for patterns in output_values:
        for pattern in patterns:
            if len(pattern) == 2 or len(pattern) == 3 or len(pattern) == 4 or len(pattern) == 7:
                answer += 1

    return answer


def part_two(signal_patterns_output_value):
    signal_patterns, output_values = signal_patterns_output_value

    output_values_digits_list = []
    for idx, output_value in enumerate(output_values):
        digits = {0: "", 1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: "", 8: "", 9: ""}

        while len(signal_patterns[idx]) != 0:
            incorrect_digit = False
            pattern = signal_patterns[idx].pop()
            if len(pattern) == 2:
                digits[1] = pattern
            elif len(pattern) == 3:
                digits[7] = pattern
            elif len(pattern) == 4:
                digits[4] = pattern
            elif len(pattern) == 7:
                digits[8] = pattern
            else:
                if len(pattern) == 6 and digits[4] != "" and digits[9] == "":
                    for char in digits[4]:
                        if char not in pattern:
                            incorrect_digit = True
                    digits[9] = pattern if not incorrect_digit else ""
                elif len(pattern) == 6 and digits[1] != "" and digits[9] != "" and digits[0] == "":
                    for char in digits[1]:
                        if char not in pattern:
                            incorrect_digit = True
                    digits[0] = pattern if not incorrect_digit else ""
                elif len(pattern) == 6 and digits[9] != "" and digits[0] != "" and digits[6] == "":
                    digits[6] = pattern
                elif len(pattern) == 5 and digits[1] != "" and digits[3] == "":
                    for char in digits[1]:
                        if char not in pattern:
                            incorrect_digit = True
                    digits[3] = pattern if not incorrect_digit else ""
                elif len(pattern) == 5 and digits[6] != "" and digits[5] == "":
                    for char in pattern:
                        if char not in digits[6]:
                            incorrect_digit = True
                    digits[5] = pattern if not incorrect_digit else ""
                elif len(pattern) == 5 and digits[3] != "" and digits[5] != "" and digits[2] == "":
                    digits[2] = pattern
                else:
                    incorrect_digit = True

                if incorrect_digit:
                    signal_patterns[idx].insert(0, pattern)

        full_digit = ""
        for value in output_value:
            for digit, string in digits.items():
                not_match = False
                if len(value) != len(string):
                    continue
                else:
                    for char in value:
                        if char not in string:
                            not_match = True
                            break
                    if not_match:
                        continue
                    else:
                        full_digit += str(digit)
                        break

        output_values_digits_list.append(int(full_digit))

    return sum(output_values_digits_list)


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
