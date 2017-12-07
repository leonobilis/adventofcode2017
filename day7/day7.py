import re

def p1(inp):
    all_childs = []
    for a in inp.values():
        all_childs.extend(a[1])
    for key, value in inp.items():
        if value[1] and key not in all_childs:
            return key


def p2(inp):
    root = p1(inp)
    weights(root, inp)

    for key, value in inp.items():
        if value[1]:
            child_w = [inp[v][2] for v in value[1]]
            s1 = set(child_w[1:]) - set(child_w[:-1])
            s2 = set(child_w[:-1]) - set(child_w[1:])
            s3 = set(child_w[1:]) & set(child_w[:-1])
            if s1:
                diff_val = s1.pop()
            elif s2:
                diff_val = s2.pop()
            else:
                continue
            diff_key = list(filter(lambda x: inp[x][2] == diff_val, value[1]))[0]
            return inp[diff_key][0] - (diff_val - s3.pop())

def weights(key, inp):
    if len(inp[key]) == 3:
        return inp(key[2])
    elif not len(inp[key][1]):
        inp[key].append(inp[key][0])
        return inp[key][0]
    elif len(inp[key][1]):
        summ = sum([weights(k, inp) for k in inp[key][1]]) + inp[key][0]
        inp[key].append(summ)
        return summ




def parse_input(inp):
    out = {}
    for a in inp.splitlines():
        s = re.search(r"([a-z]+) \(([\d]+)\)( -> ([a-z, ]+)|())", a)
        out[s.group(1)] = [int(s.group(2)), s.group(4).split(', ') if s.group(4) else []]
    return out


if __name__ == "__main__":

    inp = parse_input("""pbga (66)
                        xhth (57)
                        ebii (61)
                        havc (66)
                        ktlj (57)
                        fwft (72) -> ktlj, cntj, xhth
                        qoyq (66)
                        padx (45) -> pbga, havc, qoyq
                        tknk (41) -> ugml, padx, fwft
                        jptl (61)
                        ugml (68) -> gyxo, ebii, jptl
                        gyxo (61)
                        cntj (57)""")

    assert(p1(inp) == 'tknk')
    assert (p2(inp) == 60)

    with open('input.txt', "r") as f:
        inp = parse_input(f.read())
        print("Part 1: {}".format(p1(inp)))
        print("Part 2: {}".format(p2(inp)))
