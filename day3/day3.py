RIGHT = 0
UP = 1
LEFT = 2
DOWN = 3

next = [UP, LEFT, DOWN, RIGHT]


def reduce_directions(direction_list):
    return sum([abs(direction_list[RIGHT] - direction_list[LEFT]), abs(direction_list[UP] - direction_list[DOWN])])


def count_directions(num):
    direction_list = [0, 0, 0, 0]
    if num > 1:
        counter1 = 0
        counter2 = 1
        current_direction = RIGHT
        for n in range(2, num+1):
            counter1 += 1
            direction_list[current_direction] += 1
            if counter1 == counter2:
                counter1 = 0
                current_direction = next[current_direction]
                if current_direction in [RIGHT, LEFT]:
                    counter2 += 1
    return direction_list


if __name__ == "__main__":

    assert(reduce_directions(count_directions(1)) == 0)
    assert (reduce_directions(count_directions(12)) == 3)
    assert (reduce_directions(count_directions(23)) == 2)
    assert(reduce_directions(count_directions(1024)) == 31)

    print(reduce_directions(count_directions(347991)))
