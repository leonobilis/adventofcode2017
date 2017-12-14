from functools import reduce


def hash(inp):
    circural_list = list(range(256))
    lengths = [ord(i) for i in list(inp)]
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
    return reduce(lambda x, y: "{}{}".format(x, y), ["{:08b}".format(a) for a in [reduce(lambda x, y: x ^ y, i) for i in [circural_list[x:x+16] for x in range(0, 255, 16)]]])


def p1(inp):
    return sum([sum([int(a) for a in hash("{}-{}".format(inp, i))]) for i in range(128)])


def p2(inp):
    grid = [[int(a) for a in hash("{}-{}".format(inp, i))] for i in range(128)]
    processed = set()
    return sum([proc(grid, i, j, processed) for j in range(128) for i in range(128)])


def proc(grid, i, j, processed):
    if (i, j) not in processed and grid[i][j]:
        processed.add((i, j))
        proc(grid, i+1, j, processed) if i+1 < 128 else None
        proc(grid, i-1, j, processed) if i-1 >= 0 else None
        proc(grid, i, j+1, processed) if j+1 < 128 else None
        proc(grid, i, j-1, processed) if j-1 >= 0 else None
        return 1
    else:
        return 0


if __name__ == "__main__":

    assert (p1('flqrgnkx') == 8108)
    assert (p2('flqrgnkx') == 1242)

    print("Part 1: {}".format(p1('hxtvlmkl')))
    print("Part 2: {}".format(p2('hxtvlmkl')))
