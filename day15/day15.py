def p1(a, b, i):
    ga = genA(a)
    gb = genB(b)
    return sum([1 for _ in range(i) if next(ga) & 65535 == next(gb) & 65535])


def genA(i):
    while True:
        i = 16807 * i % 2147483647
        yield i


def genB(i):
    while True:
        i = 48271 * i % 2147483647
        yield i


def p2(a, b, i):
    ga = genA2(a)
    gb = genB2(b)
    return sum([1 for _ in range(i) if next(ga) & 65535 == next(gb) & 65535])


def genA2(i):
    while True:
        i = 16807 * i % 2147483647
        if i % 4 == 0:
            yield i


def genB2(i):
    while True:
        i = 48271 * i % 2147483647
        if i % 8 == 0:
            yield i


if __name__ == "__main__":

    assert (p1(65, 8921, 40000000) == 588)
    assert (p2(65, 8921, 5000000) == 309)

    print("Part 1: {}".format(p1(116, 299, 40000000)))
    print("Part 2: {}".format(p2(116, 299, 5000000)))
