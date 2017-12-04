from itertools import permutations


def check1(passphrase):
    passphrase = passphrase.split()
    return len([passphrase[i] for i in range(len(passphrase)) if passphrase[i] in passphrase[i+1:]]) == 0


def check2(passphrase):
    passphrase = passphrase.split()
    return len([passphrase[i] for i in range(len(passphrase)) if len([x for x in passphrase[i+1:] if passphrase[i] in ["".join(y) for y in permutations(x)]])]) == 0


if __name__ == "__main__":

    assert (check1('aa bb cc dd ee'))
    assert (not check1('aa bb cc dd aa'))
    assert (check1('aa bb cc dd aaa'))

    assert (check2('abcde fghij'))
    assert (not check2('abcde xyz ecdab'))
    assert (check2('a ab abc abd abf abj'))
    assert (check2('iiii oiii ooii oooi oooo'))
    assert (not check2('oiii ioii iioi iiio'))

    with open('input.txt', "r") as f:
        lines = f.read().splitlines()
        print("Part 1: {}".format(len(list(filter(lambda x: check1(x), lines)))))
        print("Part 2: {}".format(len(list(filter(lambda x: check2(x), lines)))))
