import re


def p1(inp):
    severity = 0
    positions = dict([(a, [0, True]) for a in inp.keys()])
    for ps in range(1, max(inp.keys())+1):
        for k in inp.keys():
            if positions[k][0] == inp[k] - 1 or positions[k][0] == 0: positions[k][1] = not positions[k][1]
            positions[k][0] = positions[k][0] + 1 if not positions[k][1] else positions[k][0] - 1
        if ps in inp.keys() and positions[ps][0] == 0:
            severity += ps * inp[ps]
    return severity


def p2(inp):
    cond = True
    delay = 0
    while cond:
        for ps in inp:
            a = (ps + delay) % ((inp[ps] - 1) * 2)
            b = a if inp[ps] > a else (inp[ps] - 1) * 2 - a
            cond = b == 0
            if cond:
                delay += 1
                break
    return delay


def parse_input(inp):
    out = {}
    for a in inp.splitlines():
        s = re.search(r"([\d]+): ([\d]+)", a)
        out[int(s.group(1))] = int(s.group(2))
    return out


if __name__ == "__main__":

    inp = parse_input("""0: 3
                        1: 2
                        4: 4
                        6: 4""")

    assert (p1(inp) == 24)
    assert (p2(inp) == 10)

    with open('input.txt', "r") as f:
        inp = parse_input(f.read())
        print("Part 1: {}".format(p1(inp)))
        print("Part 2: {}".format(p2(inp)))
