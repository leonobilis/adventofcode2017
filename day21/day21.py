import re


def match_pattern(grid, patterns):
    grids = [grid]
    for i in range(3):
        rotated1 = ["".join(i) for i in list(reversed(list(zip(*grids[-1]))))]
        flipped1 = grids[-1][::-1]
        flipped2 = ["".join(reversed(g)) for g in grids[-1]]
        grids.append(flipped1) if flipped1 not in grids else None
        grids.append(flipped2) if flipped2 not in grids else None
        grids.append(rotated1) if rotated1 not in grids else None
    grids.remove(grid)
    grids.append(grid)
    for i in range(3):
        rotated2 = ["".join(i) for i in list(reversed(list(zip(*grid[::-1]))))[::-1]]
        flipped1 = grids[-1][::-1]
        flipped2 = ["".join(reversed(g)) for g in grids[-1]]
        grids.append(flipped1) if flipped1 not in grids else None
        grids.append(flipped2) if flipped2 not in grids else None
        grids.append(rotated2) if rotated2 not in grids else None
    for p1, p2 in patterns:
        for g in grids:
            if g == p1:
                return p2.copy()


def p(patterns, iter):
    grid = ['.#.', '..#', '###']
    for i in range(iter):
        new_grid = []
        d = 2 if not len(grid)%2 else 3
        for y in range(0, len(grid), d):
            subgrid_y = grid[y:y+d]
            new_subgrid_y = []
            for x in range(0, len(grid), d):
                subgrid = [s[x:x+d] for s in subgrid_y]
                new_subgrid = match_pattern(subgrid, patterns)
                if x:
                    for yy in range(d+1):
                        new_subgrid_y[yy] += new_subgrid[yy]
                else:
                    new_subgrid_y = new_subgrid
            new_grid.extend(new_subgrid_y)
        grid = new_grid
    return sum([g.count('#') for g in grid])


def parse_input(inp):
    patterns = []
    for a in inp.splitlines():
        s = re.search(r"([.#/]+) => ([.#/]+)", a)
        patterns.append([s.group(1).split('/'), s.group(2).split('/')])
    return patterns


if __name__ == "__main__":

    inp = parse_input("""../.# => ##./#../...
.#./..#/### => #..#/..../..../#..#""")

    assert(p(inp, 2) == 12)

    with open('input.txt', "r") as f:
        inp = parse_input(f.read())
        print("Part 1: {}".format(p(inp, 5)))
        print("Part 2: {}".format(p(inp, 18)))
