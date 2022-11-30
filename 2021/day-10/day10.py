part_one_scoring_table = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}
part_two_scoring_table = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}
multiplier = 5


def part_one(chunks):
    global part_one_scoring_table
    answer = 0
    for chunk in chunks:
        expected_chars = []
        for char in chunk:
            if char == "(":
                expected_chars.append(")")
            elif char == "[":
                expected_chars.append("]")
            elif char == "{":
                expected_chars.append("}")
            elif char == "<":
                expected_chars.append(">")
            else:
                expected_char = expected_chars.pop()
                if expected_char != char:
                    answer += part_one_scoring_table[char]
                    break

    return answer


def part_two(chunks):
    global part_two_scoring_table, multiplier
    scores = []
    for chunk in chunks:
        expected_chars = []
        corrupted = False
        for char in chunk:
            if char == "(":
                expected_chars.append(")")
            elif char == "[":
                expected_chars.append("]")
            elif char == "{":
                expected_chars.append("}")
            elif char == "<":
                expected_chars.append(">")
            else:
                expected_char = expected_chars.pop()
                if expected_char != char:
                    corrupted = True
                    break

        if corrupted:
            continue

        score = 0
        for incomplete_char in reversed(expected_chars):
            score *= multiplier
            score += part_two_scoring_table[incomplete_char]
        scores.append(score)

    scores = sorted(scores)
    return scores[len(scores)//2]


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        _input = [list(map(str, list(line.strip()))) for line in f]

    answer1 = part_one(_input)
    print("Part one:")
    print("Answer: {}".format(int(answer1)))
    print()
    answer2 = part_two(_input)
    print("Part two:")
    print("Answer: {}".format(answer2))
