def spin(inlist, x):
    return inlist[-int(x):] + inlist[:-int(x)]


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


def dance(programs, inp):
    action = {"s": spin, "x": exchange, "p": partner}
    for i in inp:
        programs = action[i[0]](programs, i[1:])
    return programs


def p1(programs, inp):
    return "".join(dance(programs, inp))


def p2(programs, inp, i):
    programs_cpy = programs.copy()
    programs = dance(programs, inp)
    count = 1
    while programs != programs_cpy:
        count += 1
        programs = dance(programs, inp)
    for _ in range(i % count):
        programs = dance(programs, inp)
    return "".join(programs)


if __name__ == "__main__":

    inp = "s1,x3/4,pe/b".split(',')

    assert (p1(list('abcde'), inp) == 'baedc')
    assert (p2(list('abcde'), inp, 2) == 'ceadb')

    with open('input.txt', "r") as f:
        inp = f.read().split(',')
        print("Part 1: {}".format(p1(list('abcdefghijklmnop'), inp)))
        print("Part 2: {}".format(p2(list('abcdefghijklmnop'), inp, 1000000000)))
