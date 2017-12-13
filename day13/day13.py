import re


def p1(inp):
    catched = []
    for ps in inp:
        a = ps % ((inp[ps] - 1) * 2)
        b = a if inp[ps] > a else (inp[ps] - 1) * 2 - a
        catched.append(ps) if b == 0 else None
    return sum([p*inp[p] for p in catched])


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
