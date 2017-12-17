def p1(a):
    buffer = [0]
    pos = 0
    for i in range(1, 2018):
        pos = (pos+1+a) % i
        buffer.insert(pos+1, i)
    return buffer[pos+2]


def p2(a):
    pos = 0
    current = 0
    for i in range(1, 50000001):
        pos = (pos+1+a) % i
        if pos == 0:
            current = i
    return current


if __name__ == "__main__":

    assert (p1(3) == 638)

    print("Part 1: {}".format(p1(348)))
    print("Part 2: {}".format(p2(348)))
