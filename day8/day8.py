def p1(inp, reg):
    for r, a, va, rc, c, vc in inp:
        reg[r] = a(reg[r], va) if c(reg[rc], vc) else reg[r]
    return max(reg.values())


def p2(inp, reg):
    max = -1000
    for r, a, va, rc, c, vc in inp:
        reg[r] = a(reg[r], va) if c(reg[rc], vc) else reg[r]
        if reg[r] > max: max = reg[r]
    return max


def parse_input(inp):
    action = {"inc": lambda x, y: x+y, "dec": lambda x, y: x-y}
    cond = {">": lambda x, y: x>y, "<": lambda x, y: x<y, ">=": lambda x, y: x>=y, "<=": lambda x, y: x<=y, "==": lambda x, y: x==y, "!=": lambda x, y: x!=y}
    out = [[r, action[a], int(va), rc, cond[c], int(vc)] for r, a, va, _, rc, c, vc in [[j for j in i.split()] for i in inp.splitlines()]]
    registers = {}
    for r, _, _, _, _, _ in out:
        registers[r] = 0
    return out, registers


if __name__ == "__main__":

    inp, reg = parse_input("""  b inc 5 if a > 1
                                a inc 1 if b < 5
                                c dec -10 if a >= 1
                                c inc -20 if c == 10""")

    assert(p1(inp, reg.copy()) == 1)
    assert(p2(inp, reg.copy()) == 10)

    with open('input.txt', "r") as f:
        inp, reg = parse_input(f.read())
        print("Part 1: {}".format(p1(inp, reg.copy())))
        print("Part 2: {}".format(p2(inp, reg.copy())))
