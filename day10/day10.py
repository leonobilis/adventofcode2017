from functools import reduce


def e1(lengths, circural_list):
    length = len(circural_list)
    p1 = 0
    skip = 0
    for l in lengths:
        p2 = (p1 + l) % length
        if p2 > p1:
            circural_list[p1:p2] = reversed(circural_list[p1:p2])
        elif l:
            sublist = list(reversed(circural_list[p1:] + circural_list[:p2]))
            circural_list[p1:] = sublist[:length-p1]
            circural_list[:p2] = sublist[length-p1:]
        p1 = (p1 + l + skip) % length
        skip += 1
    return circural_list[0] * circural_list[1]


def e2(lengths):
    circural_list = list(range(256))
    lengths.extend([17, 31, 73, 47, 23])
    length = len(circural_list)
    p1 = 0
    skip = 0
    for l in 64 * lengths:
        p2 = (p1 + l) % length
        if p2 > p1:
            circural_list[p1:p2] = reversed(circural_list[p1:p2])
        elif l:
            sublist = list(reversed(circural_list[p1:] + circural_list[:p2]))
            circural_list[p1:] = sublist[:length-p1]
            circural_list[:p2] = sublist[length-p1:]
        p1 = (p1 + l + skip) % length
        skip += 1
    return reduce(lambda x, y: "{}{}".format(x, y), ['%x' % a if a > 16 else '0'+('%x' % a) for a in [reduce(lambda x, y: x ^ y, i) for i in [circural_list[x:x+16] for x in range(0, 255, 16)]]])


if __name__ == "__main__":

    assert (e1([3, 4, 1, 5], [0, 1, 2, 3, 4]) == 12)

    assert (e2([ord(i) for i in list("")]) == 'a2582a3a0e66e6e86e3812dcb672a272')
    assert (e2([ord(i) for i in list("AoC 2017")]) == '33efeb34ea91902bb2f59c9920caa6cd')
    assert (e2([ord(i) for i in list("1,2,3")]) == '3efbe78a8d82f29979031a4aa0b16a9d')
    assert (e2([ord(i) for i in list("1,2,4")]) == '63960835bcdc130f0b66d7ff4f6a5a8e')

    with open('input.txt', "r") as f:
        inp = f.read()
        print("Part 1: {}".format(e1([int(i) for i in inp.split(',')], list(range(256)))))
        print("Part 2: {}".format(e2([ord(i) for i in list(inp)])))
