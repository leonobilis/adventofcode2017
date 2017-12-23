def val(x, reg):
    return int(x) if x.lstrip('-').isdigit() else reg[x]


def isprime(x):
    for i in range(2, x-1):
        if x % i == 0:
            return False
    else:
        return True


def p1(inp):
    registers = {}
    counter = 0
    instructions = [[j for j in i.split()] for i in inp.splitlines()]
    for r in "abcdefgh":
        registers[r] = 0
    pos = 0
    while pos < len(instructions):
        inst = instructions[pos]
        if inst[0] == "set":
            registers[inst[1]] = val(inst[2], registers)
        elif inst[0] == "sub":
            registers[inst[1]] -= val(inst[2], registers)
        elif inst[0] == "mul":
            registers[inst[1]] *= val(inst[2], registers)
            counter += 1
        elif inst[0] == "jnz":
            if val(inst[1], registers):
                pos += val(inst[2], registers)
                continue
        pos += 1
    return counter


def p2(inp):
    registers = {'a': 1, 'b': 0, 'c': 0}
    instructions = [[j for j in i.split()] for i in inp.splitlines()]
    pos = 0
    while pos < 8:
        inst = instructions[pos]
        if inst[0] == "set":
            registers[inst[1]] = val(inst[2], registers)
        elif inst[0] == "sub":
            registers[inst[1]] -= val(inst[2], registers)
        elif inst[0] == "mul":
            registers[inst[1]] *= val(inst[2], registers)
        elif inst[0] == "jnz":
            if val(inst[1], registers):
                pos += val(inst[2], registers)
                continue
        pos += 1

    b = registers['b']
    c = registers['c']

    return sum([0 if isprime(x) else 1 for x in range(b, c+1, 17)])


if __name__ == "__main__":
    with open('input.txt', "r") as f:
        inp = f.read()
        print("Part 1: {}".format(p1(inp)))
        print("Part 2: {}".format(p2(inp)))
