from itertools import product

RIGHT = 0
UP = 1
LEFT = 2
DOWN = 3

next = [UP, LEFT, DOWN, RIGHT]
dir_val = [[1, 0], [0, 1], [-1, 0], [0, -1]]


class A:
    def __init__(self):
        self.SIZE = 100
        self.CENTER = int(self.SIZE/2)
        self.a = [[0 for _ in range(self.SIZE)] for _ in range(self.SIZE)]
        self.a[self.CENTER][self.CENTER] = 1
        self.a[self.CENTER+1][self.CENTER] = 1

        self.num = 0
        self.counter1 = 0
        self.counter2 = 1
        self.curr_dir = RIGHT
        self.num = 0
        self.x = 0
        self.y = 0

    def get(self, x, y):
        return self.a[self.CENTER+x][self.CENTER+y]

    def set(self, x, y, value):
        self.a[self.CENTER + x][self.CENTER + y] = value

    def fill(self, x, y):
        self.set(x, y, sum([self.get(x+i,y+j) for i, j in list(product([1,-1, 0], repeat=2))[:-1]]))

    def next(self):
        if self.num < 1:
            self.num += 1
            return 1
        else:
            self.counter1 += 1
            self.x += dir_val[self.curr_dir][0]
            self.y += dir_val[self.curr_dir][1]
            self.fill(self.x, self.y)
            retval = self.get(self.x, self.y)
            if self.counter1 == self.counter2:
                self.counter1 = 0
                self.curr_dir = next[self.curr_dir]
                if self.curr_dir in [RIGHT, LEFT]:
                    self.counter2 += 1
            return retval


if __name__ == "__main__":
    a = A()

    val = 0
    while val < 347991:
        val = a.next()

    print(val)
