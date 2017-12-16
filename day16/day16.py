def spin(inlist, x):
    x = int(x)
    outlist = inlist[-x:]
    outlist.extend(inlist[:-x])
    return outlist


def exchange(inlist, ab):
    a, b = ab.split('/')
    tmp = inlist[int(a)]
    inlist[int(a)] = inlist[int(b)]
    inlist[int(b)] = tmp
    return inlist


def partner(inlist, ab):
    a, b = ab.split('/')
    ia = inlist.index(a)
    ib = inlist.index(b)
    inlist[ia] = b
    inlist[ib] = a
    return inlist


def p1(programs, inp):
    action = {"s": spin, "x": exchange, "p": partner}
    for i in inp:
        programs = action[i[0]](programs, i[1:])
    return "".join(programs)


def p2(programs, inp, i):
    action = {"s": spin, "x": exchange, "p": partner}
    programs_cpy = programs.copy()
    cond = True
    count = 0
    while cond:
        count += 1
        for ii in inp:
            programs = action[ii[0]](programs, ii[1:])
        cond = programs != programs_cpy
    for _ in range(i % count):
        for ii in inp:
            programs = action[ii[0]](programs, ii[1:])
    return "".join(programs)


if __name__ == "__main__":

    inp = "s1,x3/4,pe/b".split(',')

    assert (p1(list('abcde'), inp) == 'baedc')
    assert (p2(list('abcde'), inp, 2) == 'ceadb')

    with open('input.txt', "r") as f:
        inp = f.read().split(',')
        print("Part 1: {}".format(p1(list('abcdefghijklmnop'), inp)))
        print("Part 2: {}".format(p2(list('abcdefghijklmnop'), inp, 1000000000)))
