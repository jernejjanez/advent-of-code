import operator
from collections import namedtuple
import math


Packet = namedtuple("Packet", ("version", "id", "value", "sub_packets"))


def prepare_input(file):
    return file.read().strip()


def to_binary(_hex):
    return bin(int('1' + _hex, 16))[3:]


def to_decimal(_binary):
    return int(_binary, 2)


def calculate_literal_packet(binary):
    if binary[0] == "0":
        return binary[1:5], 5
    return tuple(map(operator.add, (binary[1:5], 5), calculate_literal_packet(binary[5:])))


def get_sub_packets_by_length(binary, i):
    values = []
    offset = 15
    length_of_packets = to_decimal(binary[i:i + offset])
    i += offset
    current_length = 0
    while current_length < length_of_packets:
        value, temp_i = calculate_packet(binary, i)
        values.append(value)
        current_length += temp_i - i
        i = temp_i

    return values, i


def get_sub_packets_by_number(binary, i):
    values = []
    offset = 11
    number_of_packets = to_decimal(binary[i:i + offset])
    i += offset
    current_packet = 0
    while current_packet < number_of_packets:
        value, i = calculate_packet(binary, i)
        values.append(value)
        current_packet += 1

    return values, i


def calculate_value(_id, sub_packets):
    value = 0
    if _id == 0:
        value = 0
        for sub_packet in sub_packets:
            value += sub_packet.value
    elif _id == 1:
        value = 1
        for sub_packet in sub_packets:
            value *= sub_packet.value
    elif _id == 2:
        value = math.inf
        for sub_packet in sub_packets:
            if value > sub_packet.value:
                value = sub_packet.value
    elif _id == 3:
        value = -1
        for sub_packet in sub_packets:
            if value < sub_packet.value:
                value = sub_packet.value
    else:
        first_sub_packet = sub_packets[0]
        second_sub_packet = sub_packets[1]
        if _id == 5:
            if first_sub_packet.value > second_sub_packet.value:
                value = 1
            else:
                value = 0
        if _id == 6:
            if first_sub_packet.value < second_sub_packet.value:
                value = 1
            else:
                value = 0
        if _id == 7:
            if first_sub_packet.value == second_sub_packet.value:
                value = 1
            else:
                value = 0

    return value


def calculate_packet(binary, i):
    version = to_decimal(binary[i:i+3])
    _id = to_decimal(binary[i + 3:i + 6])
    i += 6
    if _id == 4:
        value, temp_i = calculate_literal_packet(binary[i:])
        i += temp_i
        return Packet(version, _id, to_decimal(value), []), i
    else:
        length_type = binary[i]
        i += 1
        if length_type == "0":
            sub_packets, i = get_sub_packets_by_length(binary, i)
        else:
            sub_packets, i = get_sub_packets_by_number(binary, i)

        value = calculate_value(_id, sub_packets)

        return Packet(version, _id, value, sub_packets), i


def sum_versions(packet):
    total = packet.version
    for sub_packet in packet.sub_packets:
        total += sum_versions(sub_packet)
    return total


def part_one(_hex):
    binary = to_binary(_hex)
    outer_packet = calculate_packet(binary, 0)[0]
    return sum_versions(outer_packet)


def part_two(_hex):
    binary = to_binary(_hex)
    outer_packet = calculate_packet(binary, 0)[0]
    return outer_packet.value


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
