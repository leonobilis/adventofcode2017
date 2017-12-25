def A(value):
    return (0, -1, B) if value else (1, 1, B)


def B(value):
    return (1, -1, B) if value else (0, 1, C)


def C(value):
    return (0, -1, A) if value else (1, 1, D)


def D(value):
    return (1, -1, F) if value else (1, -1, E)


def E(value):
    return (0, -1, D) if value else (1, -1, A)


def F(value):
    return (1, -1, E) if value else (1, 1, A)


def p1(steps):
    tape = [0 for _ in range(5000)]
    pos = 5000//2
    state = A
    for _ in range(steps):
        tape[pos], p, state = state(tape[pos])
        pos += p
    return sum(tape)


if __name__ == "__main__":
        print("Part 1: {}".format(p1(12629077)))
