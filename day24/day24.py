from functools import reduce


def count(pin, port, ports, counter):
        ports.remove(port)
        counter += port[0] + port[1]
        return max(max([count(p[0], p, ports.copy(), counter) for p in ports if p[1] == pin]+[counter]), max([count(p[1], p, ports.copy(), counter) for p in ports if p[0] == pin]+[counter]))


def p1(inp):
    ports = [[int(j) for j in i.split('/')] for i in inp.splitlines()]
    return max(max([count(p[0], p, ports.copy(), 0) for p in ports if p[1] == 0]+[0]), max([count(p[1], p, ports.copy(), 0) for p in ports if p[0] == 0]+[0]))


def create_bridge(pin, port, ports, bridge):
    ports.remove(port)
    bridge.append(port[0] + port[1])
    a = sorted(reduce(lambda x, y: x+y, [create_bridge(p[0], p, ports.copy(), bridge.copy()) for p in ports if p[1] == pin], [[]]), key=lambda x: len(x), reverse=True)
    b = sorted(reduce(lambda x, y: x+y, [create_bridge(p[1], p, ports.copy(), bridge.copy()) for p in ports if p[0] == pin], [[]]), key=lambda x: len(x), reverse=True)
    return list(filter(lambda x: len(x) == max(len(a[0]), len(b[0]), len(bridge)), a+b+[bridge]))


def p2(inp):
    ports = [[int(j) for j in i.split('/')] for i in inp.splitlines()]
    a = sorted(reduce(lambda x, y: x+y, [create_bridge(p[0], p, ports.copy(), []) for p in ports if p[1] == 0], [[]]), key=lambda x: len(x), reverse=True)
    b = sorted(reduce(lambda x, y: x+y, [create_bridge(p[1], p, ports.copy(), []) for p in ports if p[0] == 0], [[]]), key=lambda x: len(x), reverse=True)
    return sum(max(filter(lambda x: len(x) == max(len(a[0]), len(b[0])), a+b), key=lambda x: sum(x)))


if __name__ == "__main__":

    inp = """0/2
            2/2
            2/3
            3/4
            3/5
            0/1
            10/1
            9/10"""

    assert (p1(inp) == 31)
    assert (p2(inp) == 19)

    with open('input.txt', "r") as f:
        inp = f.read()
        print("Part 1: {}".format(p1(inp)))
        print("Part 2: {}".format(p2(inp)))
