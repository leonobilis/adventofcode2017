down = (1, 0)
up = (-1, 0)
right = (0, 1)
left = (0, -1)


def p1(inp):
    direction = down
    letters = ""
    y = 0
    x = inp[y].index('|')
    end = False

    while not end:
        s = inp[y][x]
        if s == "-" or s == "|":
            y += direction[0]
            x += direction[1]
        elif s.isupper():
            letters += s
            y += direction[0]
            x += direction[1]
        elif s == "+":
            if direction != up and y+1 < len(inp) and (inp[y+1][x] == "|" or inp[y+1][x].isupper()):
                direction = down
            elif direction != down and y-1 >= 0 and (inp[y-1][x] == "|" or inp[y-1][x].isupper()):
                direction = up
            elif direction != left and x+1 < len(inp[y]) and (inp[y][x+1] == "-" or inp[y][x+1].isupper()):
                direction = right
            elif direction != right and x-1 >= 0 and (inp[y][x-1] == "-" or inp[y][x-1].isupper()):
                direction = left
            else:
                end = True
            y += direction[0]
            x += direction[1]
        else:
            end = True
    return letters


def p2(inp):
    direction = down
    count = 0
    y = 0
    x = inp[y].index('|')
    end = False

    while not end:
        s = inp[y][x]
        if s == "-" or s == "|" or s.isupper():
            y += direction[0]
            x += direction[1]
            count += 1
        elif s == "+":
            if direction != up and y+1 < len(inp) and (inp[y+1][x] == "|" or inp[y+1][x].isupper()):
                direction = down
            elif direction != down and y-1 >= 0 and (inp[y-1][x] == "|" or inp[y-1][x].isupper()):
                direction = up
            elif direction != left and x+1 < len(inp[y]) and (inp[y][x+1] == "-" or inp[y][x+1].isupper()):
                direction = right
            elif direction != right and x-1 >= 0 and (inp[y][x-1] == "-" or inp[y][x-1].isupper()):
                direction = left
            else:
                end = True
            count += 1
            y += direction[0]
            x += direction[1]
        else:
            end = True
    return count


if __name__ == "__main__":

    inp = """     |.......
     |  +--+
     A  |  C.........
 F---|----E|--+......
     |  |  |  D......
     +B-+  +--+ """.replace(' ', '.').splitlines()

    assert (p1(inp) == 'ABCDEF')
    assert (p2(inp) == 38)

    with open('input.txt', "r") as f:
        inp = f.read().replace(' ', '.').splitlines()
        print("Part 1: {}".format(p1(inp)))
        print("Part 2: {}".format(p2(inp)))
