from collections import deque


def val(x, reg):
    return int(x) if x.lstrip('-').isdigit() else reg[x]


def p1(inp):
    registers = {}
    snd_val = 0
    instructions = [[j for j in i.split()] for i in inp.splitlines()]
    for r in instructions:
        registers[r[1]] = 0
    pos = 0
    while pos < len(instructions):
        inst = instructions[pos]
        if inst[0] == "snd":
            snd_val = registers[inst[1]]
        elif inst[0] == "set":
            registers[inst[1]] = val(inst[2], registers)
        elif inst[0] == "add":
            registers[inst[1]] += val(inst[2], registers)
        elif inst[0] == "mul":
            registers[inst[1]] *= val(inst[2], registers)
        elif inst[0] == "mod":
            registers[inst[1]] %= val(inst[2], registers)
        elif inst[0] == "rcv":
            if registers[inst[1]]:
                return snd_val
        elif inst[0] == "jgz":
            if val(inst[1], registers) > 0:
                pos += val(inst[2], registers)
                continue
        pos += 1
    return 0


def p2(inp):
    registers1 = {}
    instructions1 = [[j for j in i.split()] for i in inp.splitlines()]
    instructions2 = instructions1.copy()
    for r in instructions1:
        if not r[1].lstrip('-').isdigit(): registers1[r[1]] = 0
    registers2 = registers1.copy()
    registers2['p'] = 1
    pos = [0, 0]
    q1 = deque()
    q2 = deque()

    instructions = instructions1
    registers = registers1
    curr_pos = 0
    snd_q = q2
    rcv_q = q1
    counter = 0

    while not(instructions1[pos[0]][0] == 'rcv' and instructions2[pos[1]][0] == 'rcv' and not len(q1) and not len(q2)) and pos[0] < len(instructions) and pos[1] < len(instructions):
        inst = instructions[pos[curr_pos]]
        if inst[0] == "snd":
            snd_q.append(val(inst[1], registers))
            if curr_pos:
                counter += 1
        elif inst[0] == "set":
            registers[inst[1]] = val(inst[2], registers)
        elif inst[0] == "add":
            registers[inst[1]] += val(inst[2], registers)
        elif inst[0] == "mul":
            registers[inst[1]] *= val(inst[2], registers)
        elif inst[0] == "mod":
            registers[inst[1]] %= val(inst[2], registers)
        elif inst[0] == "rcv":
            if len(rcv_q):
                registers[inst[1]] = rcv_q.popleft()
            else:
                if curr_pos:
                    instructions = instructions1
                    registers = registers1
                    curr_pos = 0
                    snd_q = q2
                    rcv_q = q1
                else:
                    instructions = instructions2
                    registers = registers2
                    curr_pos = 1
                    snd_q = q1
                    rcv_q = q2
                continue
        elif inst[0] == "jgz":
            if val(inst[1], registers) > 0:
                pos[curr_pos] += val(inst[2], registers)
                continue
        pos[curr_pos] += 1
    return counter


if __name__ == "__main__":

    inp = ("""set a 1
                add a 2
                mul a a
                mod a 5
                snd a
                set a 0
                rcv a
                jgz a -1
                set a 1
                jgz a -2""")

    assert(p1(inp) == 4)

    inp = ("""snd 1
                snd 2
                snd p
                rcv a
                rcv b
                rcv c
                rcv d
                add c 5""")

    assert (p2(inp) == 3)

    with open('input.txt', "r") as f:
        inp = f.read()
        print("Part 1: {}".format(p1(inp)))
        print("Part 2: {}".format(p2(inp)))
