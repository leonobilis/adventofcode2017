import re


def dist(pos):
    return sum([abs(p) for p in pos])


def p1(inp):
    return min(list(filter(lambda x: dist(x['a']) == dist(min(inp, key=lambda x: dist(x['a']))['a']), inp)), key=lambda x: dist(x['v']))['i']


def p2(inp):
    no_change_counter = 0
    while no_change_counter < 100:
        positions = []
        for i in inp:
            i['v'] = [i['v'][j] + i['a'][j] for j in range(3)]
            i['p'] = [i['p'][j] + i['v'][j] for j in range(3)]
            positions.append(i['p'])
        no_change_counter = 0 if list(map(lambda x: inp.remove(x), list(filter(lambda y: positions.count(y['p']) > 1, inp)))) else no_change_counter + 1
    return len(inp)


def parse_input(inp):
    particles = []
    i = 0
    for a in inp.splitlines():
        s = re.search(r"p=<([-\d]+),([-\d]+),([-\d]+)>, v=<([-\d]+),([-\d]+),([-\d]+)>, a=<([-\d]+),([-\d]+),([-\d]+)>", a)
        particles.append({'p': [int(s.group(1)), int(s.group(2)), int(s.group(3))], 'v': [int(s.group(4)), int(s.group(5)), int(s.group(6))], 'a': [int(s.group(7)), int(s.group(8)), int(s.group(9))], 'i': i})
        i += 1
    return particles


if __name__ == "__main__":

    inp = parse_input("""p=<3,0,0>, v=<2,0,0>, a=<-1,0,0>
                        p=<4,0,0>, v=<0,0,0>, a=<-2,0,0>""")
    assert(p1(inp) == 0)

    inp = parse_input("""p=<-6,0,0>, v=<3,0,0>, a=<0,0,0>
                        p=<-4,0,0>, v=<2,0,0>, a=<0,0,0>
                        p=<-2,0,0>, v=<1,0,0>, a=<0,0,0>
                        p=<3,0,0>, v=<-1,0,0>, a=<0,0,0>""")
    assert (p2(inp) == 1)

    with open('input.txt', "r") as f:
        inp = parse_input(f.read())
        print("Part 1: {}".format(p1(inp.copy())))
        print("Part 2: {}".format(p2(inp.copy())))
