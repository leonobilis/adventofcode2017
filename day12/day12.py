import re


def p1(inp):
    keys = [0]
    to_process = [0]
    while len(to_process):
        for k in inp[to_process.pop()]:
            if k not in to_process and k not in keys:
                to_process.append(k)
                keys.append(k)
    return len(keys)


def p2(inp):
    keys = set()
    all_keys = set(inp.keys())
    groups = 0
    diff_set = all_keys
    while diff_set:
        to_process = [diff_set.pop()]
        groups += 1
        while len(to_process):
            for k in inp[to_process.pop()]:
                if k not in to_process and k not in keys:
                    to_process.append(k)
                    keys.add(k)
        diff_set = all_keys - keys
    return groups


def parse_input(inp):
    out = {}
    for a in inp.splitlines():
        s = re.search(r"([\d]+) <-> ([\d, ]+)", a)
        out[int(s.group(1))] = [int(b) for b in s.group(2).split(', ')]
    return out


if __name__ == "__main__":

    inp = parse_input("""0 <-> 2
                        1 <-> 1
                        2 <-> 0, 3, 4
                        3 <-> 2, 4
                        4 <-> 2, 3, 6
                        5 <-> 6
                        6 <-> 4, 5""")

    assert (p1(inp) == 6)
    assert (p2(inp) == 2)

    with open('input.txt', "r") as f:
        pass
        inp = parse_input(f.read())
        print("Part 1: {}".format(p1(inp)))
        print("Part 2: {}".format(p2(inp)))
