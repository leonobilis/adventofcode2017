from copy import deepcopy

down = (1, 0)
up = (-1, 0)
right = (0, 1)
left = (0, -1)

turn_left = {up: left, down: right, right: up, left: down}
turn_right = {up: right, down: left, right: down, left: up}
reverse = {up: down, down: up, right: left, left: right}


def p1(grid, iter):
    direction = up
    pos = [len(grid)//2, len(grid)//2]
    counter = 0
    for i in range(iter):
        if grid[pos[0]][pos[1]]:
            direction = turn_right[direction]
        else:
            direction = turn_left[direction]
            counter += 1
        grid[pos[0]][pos[1]] = not grid[pos[0]][pos[1]]
        pos = [pos[0] + direction[0], pos[1] + direction[1]]
    return counter


def p2(grid, iter):
    direction = up
    pos = [len(grid)//2, len(grid)//2]
    counter = 0
    for i in range(iter):
        if grid[pos[0]][pos[1]] == '.':
            grid[pos[0]][pos[1]] = 'W'
            direction = turn_left[direction]
        elif grid[pos[0]][pos[1]] == 'W':
            grid[pos[0]][pos[1]] = '#'
            counter += 1
        elif grid[pos[0]][pos[1]] == '#':
            grid[pos[0]][pos[1]] = 'F'
            direction = turn_right[direction]
        else:
            grid[pos[0]][pos[1]] = '.'
            direction = reverse[direction]
        pos = [pos[0] + direction[0], pos[1] + direction[1]]
    return counter


def parse_input(inp):
    grid_len = 500
    grid = [[False for _ in range(grid_len)] for _ in range(grid_len)]
    inner_grid = [[True if b == '#' else False for b in a] for a in inp.splitlines()]
    for i in range(len(inner_grid)):
        grid[grid_len//2 - len(inner_grid)//2 + i][grid_len//2 - len(inner_grid)//2:grid_len//2 - len(inner_grid)//2 + len(inner_grid)] = inner_grid[i]
    return grid


def parse_input2(inp):
    grid_len = 500
    grid = [['.' for _ in range(grid_len)] for _ in range(grid_len)]
    inner_grid = [list(a) for a in inp.splitlines()]
    for i in range(len(inner_grid)):
        grid[grid_len//2 - len(inner_grid)//2 + i][grid_len//2 - len(inner_grid)//2:grid_len//2 - len(inner_grid)//2 + len(inner_grid)] = inner_grid[i]
    return grid


if __name__ == "__main__":

    inp = parse_input("..#\n#..\n...")

    assert (p1(deepcopy(inp), 7) == 5)
    assert (p1(deepcopy(inp), 70) == 41)
    assert (p1(deepcopy(inp), 10000) == 5587)

    inp = parse_input2("..#\n#..\n...")

    assert (p2(deepcopy(inp), 100) == 26)
    assert (p2(deepcopy(inp), 10000000) == 2511944)

    with open('input.txt', "r") as f:
        inp = f.read()
        print("Part 1: {}".format(p1(parse_input(inp), 10000)))
        print("Part 1: {}".format(p2(parse_input2(inp), 10000000)))
