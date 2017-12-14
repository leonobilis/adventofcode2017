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
    grid = [[int(a) for a in hash("{}-{}".format(inp, k))] for k in range(128)]
    return sum([proc(grid, i, j) for j in range(128) for i in range(128)])


def proc(grid, i, j):
    if grid[i][j]:
        grid[i][j] = 0
        [proc(grid, i+ii, j+jj) for ii, jj in [(0, 1), (1, 0), (0, -1), (-1, 0)] if 0 <= i+ii < 128 and 0 <= j+jj < 128]
        return 1
    else:
        return 0


if __name__ == "__main__":

    assert (p1('flqrgnkx') == 8108)
    assert (p2('flqrgnkx') == 1242)

    print("Part 1: {}".format(p1('hxtvlmkl')))
    print("Part 2: {}".format(p2('hxtvlmkl')))
