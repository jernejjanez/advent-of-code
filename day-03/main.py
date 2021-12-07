import copy


def string_to_int(number_string):
    return int(number_string)


def part_one(binary_list):
    bit_dict = {i: 0 for i, _ in enumerate(binary_list[0])}
    for binary in binary_list:
        for i, bit in enumerate(binary):
            if bit == 1:
                bit_dict[i] += 1
            else:
                bit_dict[i] -= 1

    gamma_rate = ""
    epsilon_rate = ""
    for _, value in bit_dict.items():
        if value > 0:
            gamma_rate += "1"
            epsilon_rate += "0"
        else:
            gamma_rate += "0"
            epsilon_rate += "1"

    gamma_rate = int(gamma_rate, 2)
    epsilon_rate = int(epsilon_rate, 2)
    print("Part one:")
    print("Gamma rate: {}".format(gamma_rate))
    print("Epsilon rate: {}".format(epsilon_rate))
    print("Answer: {}".format(gamma_rate * epsilon_rate))


def list_to_string(array):
    str1 = ""

    for ele in array:
        str1 += str(ele)

    return str1


def oxygen_generator_rating(binary_list):
    binary_list_copy = copy.deepcopy(binary_list)
    for i, _ in enumerate(binary_list_copy[0]):
        index_0 = []
        index_1 = []
        bit_sum = 0
        for index, binary in enumerate(binary_list_copy):
            if binary[i] == 1:
                index_1.append(index)
                bit_sum += 1
            else:
                index_0.append(index)
                bit_sum -= 1

        if len(binary_list_copy) == 1:
            break
        elif bit_sum >= 0:
            binary_list_copy = [ele for idx, ele in enumerate(binary_list_copy) if idx not in index_0]
        else:
            binary_list_copy = [ele for idx, ele in enumerate(binary_list_copy) if idx not in index_1]

    return binary_list_copy[0]


def co2_scrubber_rating(binary_list):
    binary_list_copy = copy.deepcopy(binary_list)
    for i, _ in enumerate(binary_list_copy[0]):
        index_0 = []
        index_1 = []
        bit_sum = 0
        for index, binary in enumerate(binary_list_copy):
            if binary[i] == 1:
                index_1.append(index)
                bit_sum += 1
            else:
                index_0.append(index)
                bit_sum -= 1

        if len(binary_list_copy) == 1:
            break
        elif bit_sum >= 0:
            binary_list_copy = [ele for idx, ele in enumerate(binary_list_copy) if idx not in index_1]
        else:
            binary_list_copy = [ele for idx, ele in enumerate(binary_list_copy) if idx not in index_0]

    return binary_list_copy[0]


def part_two(report):
    oxygen_generator_rating_binary = oxygen_generator_rating(report)
    co2_scrubber_rating_binary = co2_scrubber_rating(report)

    oxygen_rating = list_to_string(oxygen_generator_rating_binary)
    co2_rating = list_to_string(co2_scrubber_rating_binary)

    print("Part two:")
    print("Oxygen generator rating binary: {}".format(oxygen_rating))
    print("CO2 scrubber rating binary: {}".format(co2_rating))

    oxygen_rating = int(oxygen_rating, 2)
    co2_rating = int(co2_rating, 2)

    print("Oxygen generator rating decimal: {}".format(oxygen_rating))
    print("CO2 scrubber rating decimal: {}".format(co2_rating))
    print("Answer: {}".format(oxygen_rating * co2_rating))


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        diagnostic_report = [list(map(string_to_int, list(line.strip()))) for line in f]

part_one(diagnostic_report)
print()
part_two(diagnostic_report)
