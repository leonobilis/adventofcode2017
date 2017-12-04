from itertools import cycle
import os


def p1(input):
    input_cycle = cycle(input)
    next(input_cycle)
    return sum(map(lambda x: int(x[0]), filter(lambda x: x[0] == x[1], [[i, next(input_cycle)] for i in input])))


def p2(input):
    input_cycle = cycle(input)
    [next(input_cycle) for _ in range(int(len(input) / 2))]
    return sum(map(lambda x: int(x[0]), filter(lambda x: x[0] == x[1], [[i, next(input_cycle)] for i in input])))


if __name__ == "__main__":

    assert (p1('1122') == 3)
    assert (p1('1111') == 4)
    assert (p1('1234') == 0)
    assert (p1('91212129') == 9)

    assert (p2('1212') == 6)
    assert (p2('1221') == 0)
    assert (p2('123425') == 4)
    assert (p2('123123') == 12)
    assert (p2('12131415') == 4)

    with open('input.txt', "r") as f:
        inp = f.readline()
        print("Part 1: {}".format(p1(inp)))
        print("Part 2: {}".format(p2(inp)))
