def reduce1(steps):
    red = [['nw', 'ne', 'n'], ['se', 'sw', 's'], ['n', 'se', 'ne'], ['s', 'nw', 'sw'], ['ne', 's', 'se'], ['sw', 'n', 'nw']]
    sum1 = sum(steps.values())
    sum2 = 0
    while sum1 != sum2:
        sum1 = sum2
        for r in red:
            if steps[r[0]] > steps[r[1]]:
                steps[r[0]] -= steps[r[1]]
                steps[r[2]] += steps[r[1]]
                steps[r[1]] = 0
            elif steps[r[1]] > steps[r[0]]:
                steps[r[1]] -= steps[r[0]]
                steps[r[2]] += steps[r[0]]
                steps[r[0]] = 0
            else:
                steps[r[2]] += steps[r[1]]
                steps[r[1]] = 0
                steps[r[0]] = 0
        sum2 = sum(steps.values())
    return steps


def reduce2(steps):
    red = [['s', 'n'], ['ne', 'sw'], ['se', 'nw']]
    for r in red:
        if steps[r[0]] > steps[r[1]]:
            steps[r[0]] -= steps[r[1]]
        elif steps[r[1]] > steps[r[0]]:
            steps[r[1]] -= steps[r[0]]
        else:
            steps[r[0]] = 0
            steps[r[1]] = 0
    return steps


def e1(path):
    steps = {'n': 0, 'ne': 0, 'se': 0, 's': 0, 'sw': 0, 'nw': 0}
    for p in path:
        steps[p] += 1
    return sum(reduce2(reduce1(steps)).values())


def e2(path):
    steps = {'n': 0, 'ne': 0, 'se': 0, 's': 0, 'sw': 0, 'nw': 0}
    maxmax = 0
    for p in path:
        steps[p] += 1
        m = sum(reduce2(reduce1(steps.copy())).values())
        maxmax = m if m > maxmax else maxmax
    return maxmax


if __name__ == "__main__":

    assert (e1(['ne','ne','ne']) == 3)
    assert (e1(['ne','ne','sw','sw']) == 0)
    assert (e1(['ne','ne','s','s']) == 2)
    assert (e1(['se','sw','se','sw','sw']) == 3)

    with open('input.txt', "r") as f:
        inp = f.read()
        print("Part 1: {}".format(e1([i for i in inp.split(',')])))
        print("Part 2: {}".format(e2([i for i in inp.split(',')])))
