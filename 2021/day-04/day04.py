import numpy as np
import copy


def prepare_boards(file):
    _boards = []
    board_number = -1
    create_new_board = True
    current_row = 0
    _drawn_numbers = []
    for idx, line in enumerate(file):
        if idx == 0:
            _drawn_numbers = list(map(int, line.strip().split(",")))
        else:
            row = list(map(int, line.strip().split()))

            if len(row) == 0:
                create_new_board = True
                board_number += 1
            else:
                if create_new_board:
                    _boards.append(np.zeros((len(row), len(row))))
                    create_new_board = False
                    current_row = 0

                _boards[board_number][current_row] = np.array(row)
                current_row += 1

    return _drawn_numbers, _boards


def part_one(_boards, _drawn_numbers):
    boards_copy = copy.deepcopy(_boards)
    user_won = False
    for number in _drawn_numbers:
        if user_won:
            break
        for i in range(0, len(boards_copy)):
            boards_copy[i][boards_copy[i] == number] = -100

            column_sums = np.sum(boards_copy[i], axis=0)
            row_sums = np.sum(boards_copy[i], axis=1)

            if -500 in column_sums or -500 in row_sums:
                boards_copy[i][boards_copy[i] == -100] = 0
                sum_of_all_unmarked_numbers = int(np.sum(boards_copy[i]))
                user_won = True

                print("Part one:")
                print("Sum of all unmarked numbers: {}".format(sum_of_all_unmarked_numbers))
                print("Winning number: {}".format(number))
                print("Answer: {}".format(sum_of_all_unmarked_numbers * number))
                break


def part_two(_boards, _drawn_numbers):
    boards_copy = copy.deepcopy(_boards)
    squid_won = False
    for number in _drawn_numbers:
        if squid_won:
            break
        offset = 0
        for i in range(0, len(boards_copy)):
            i_offset = i - offset
            boards_copy[i_offset][boards_copy[i_offset] == number] = -100

            column_sums = np.sum(boards_copy[i_offset], axis=0)
            row_sums = np.sum(boards_copy[i_offset], axis=1)

            if -500 in column_sums or -500 in row_sums:
                if len(boards_copy) > 1:
                    boards_copy.pop(i_offset)
                    offset += 1
                    continue
                else:
                    boards_copy[i_offset][boards_copy[i_offset] == -100] = 0
                    sum_of_all_unmarked_numbers = int(np.sum(boards_copy[i_offset]))
                    squid_won = True

                    print("Part two:")
                    print("Sum of all unmarked numbers: {}".format(sum_of_all_unmarked_numbers))
                    print("Winning number: {}".format(number))
                    print("Answer: {}".format(sum_of_all_unmarked_numbers * number))
                    break


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        drawn_numbers, boards = prepare_boards(f)

    part_one(boards, drawn_numbers)
    print()
    part_two(boards, drawn_numbers)
