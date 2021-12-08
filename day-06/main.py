import copy


# Naive solution
def part_one(lanternfish_timers, _number_of_days):
    for day in range(_number_of_days):
        for i in range(len(lanternfish_timers)):
            if lanternfish_timers[i] == 0:
                lanternfish_timers[i] = 6
                lanternfish_timers.append(8)
            else:
                lanternfish_timers[i] -= 1

    return len(lanternfish_timers)


# Robust solution using dictionaries
def part_two(lanternfish_timers, _number_of_days):
    lanternfish_timers_dict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}

    for lanternfish in lanternfish_timers:
        lanternfish_timers_dict[lanternfish] += 1

    for day in range(_number_of_days):
        updated_lanternfish_timers_dict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
        for key, value in lanternfish_timers_dict.items():
            if key == 0:
                updated_lanternfish_timers_dict[8] += value
                updated_lanternfish_timers_dict[6] += value
            else:
                updated_lanternfish_timers_dict[key-1] += value
        lanternfish_timers_dict = updated_lanternfish_timers_dict

    return sum(lanternfish_timers_dict.values())


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lanternfish_list = [list(map(int, line.strip().split(","))) for line in f][0]

    number_of_days1 = 80
    answer1 = part_one(copy.deepcopy(lanternfish_list), number_of_days1)
    print("Part one:")
    print("Answer: {}".format(answer1))
    print()
    number_of_days2 = 256
    answer2 = part_two(copy.deepcopy(lanternfish_list), number_of_days2)
    print("Part two:")
    print("Answer: {}".format(answer2))
