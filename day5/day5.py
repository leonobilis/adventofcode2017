def step1(input):
    pos = 0
    step = 0
    while 0 <= pos < len(input):
        tmp = input[pos]
        input[pos] += 1
        pos += tmp
        step += 1
    return step


def step2(input):
    pos = 0
    step = 0
    while 0 <= pos < len(input):
        tmp = input[pos]
        if tmp >= 3:
            input[pos] -= 1
        else:
            input[pos] += 1
        pos += tmp
        step += 1
    return step


if __name__ == "__main__":

    assert (step1([0, 3, 0, 1, -3]) == 5)
    assert (step2([0, 3, 0, 1, -3]) == 10)

    with open('input.txt', "r") as f:
        inp = [int(lines) for lines in f.read().splitlines()]
        print("Part 1: {}".format(step1(inp.copy())))
        print("Part 2: {}".format(step2(inp.copy())))
