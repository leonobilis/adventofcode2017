def p1(inp):
    opened = []
    group_score = 1
    score = 0
    garbage=False
    ignore=False
    for i in inp:
        if ignore:
            ignore = False
            continue
        elif i=='!':
            ignore = True
        elif garbage:
            if i=='>':
                garbage = False
        else:
            if i=='<':
                garbage = True
            elif i=='{':
                opened.append(group_score)
                group_score += 1
            elif i=='}':
                score += opened.pop()
                group_score -= 1
    return score


def p2(inp):
    garbage_counter = 0
    garbage = False
    ignore = False
    for i in inp:
        if ignore:
            ignore = False
            continue
        elif i == '!':
            ignore = True
        elif garbage:
            if i == '>':
                garbage = False
            else:
                garbage_counter += 1
        else:
            if i == '<':
                garbage = True
    return garbage_counter


if __name__ == "__main__":

    assert(p1("{}") == 1)
    assert (p1("{{{}}}") == 6)
    assert (p1("{{},{}}") == 5)
    assert (p1("{{{},{},{{}}}}") == 16)
    assert (p1("{<a>,<a>,<a>,<a>}") == 1)
    assert (p1("{{<ab>},{<ab>},{<ab>},{<ab>}}") == 9)
    assert (p1("{{<!!>},{<!!>},{<!!>},{<!!>}}") == 9)
    assert (p1("{{<a!>},{<a!>},{<a!>},{<ab>}}") == 3)

    assert (p2("<>") == 0)
    assert (p2("<random characters>") == 17)
    assert (p2("<<<<>") == 3)
    assert (p2("<{!>}>") == 2)
    assert (p2("<!!>") == 0)
    assert (p2("<!!!>>") == 0)
    assert (p2('<{o"i!a,<{i<a>') == 10)

    with open('input.txt', "r") as f:
        inp = f.read()
        print("Part 1: {}".format(p1(inp)))
        print("Part 2: {}".format(p2(inp)))
