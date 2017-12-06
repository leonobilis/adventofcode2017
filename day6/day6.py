def r1(input):
    input_len = len(input)
    reached = []
    counter = 0
    while not list(filter(lambda r: len([i for i, j in zip(input, r) if i == j]) == input_len, reached)):
        reached.append(input.copy())
        counter += 1
        to_redist = input.index(max(input))
        redist_val = input[to_redist]
        input[to_redist] = 0
        for i in range(redist_val):
            to_redist = 0 if to_redist + 1 == input_len else to_redist + 1
            input[to_redist] += 1

    return counter


def r2(input):
    input_len = len(input)
    reached = []
    counter = 0
    seen_before = input.copy()
    cond = True
    while cond:
        reached.append([input.copy(), counter])
        counter += 1
        to_redist = input.index(max(input))
        redist_val = input[to_redist]
        input[to_redist] = 0
        for i in range(redist_val):
            to_redist = 0 if to_redist + 1 == input_len else to_redist + 1
            input[to_redist] += 1

        seen_before = list(filter(lambda r: len([i for i, j in zip(input, r[0]) if i == j]) == input_len, reached))
        cond = not seen_before

    return counter - seen_before[0][1]


if __name__ == "__main__":
    assert (r1([0, 2, 7, 0]) == 5)
    assert (r2([0, 2, 7, 0]) == 4)

    print("Part 1: {}".format(r1([11, 11, 13, 7, 0, 15, 5, 5, 4, 4, 1, 1, 7, 1, 15, 11])))
    print("Part 2: {}".format(r2([11, 11, 13, 7, 0, 15, 5, 5, 4, 4, 1, 1, 7, 1, 15, 11])))
