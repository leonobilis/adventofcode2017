def p1(input):
    return sum([max(i) - min(i) for i in input])


def p2(input):
    return sum([[a / b[0] for [a, b] in filter(lambda x: x[1], map(lambda j: [j, list(filter(lambda k: j % k == 0 and j != k, i))], i))][0] for i in input])

if __name__ == "__main__":

    example = """5 1 9 5
                7 5 3
                2 4 6 8""".split('\n')

    assert (p1([[int(j) for j in i.split()] for i in example]) == 18)

    example2 = """5 9 2 8
                9 4 7 3
                3 8 6 5""".split('\n')

    assert (p2([[int(j) for j in i.split()] for i in example2]) == 9)

    with open('input.txt', "r") as f:
        inp = [[int(j) for j in i.split()] for i in f.read().splitlines()]
        print("Part 1: {}".format(p1(inp)))
        print("Part 2: {}".format(p2(inp)))
