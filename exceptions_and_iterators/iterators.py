"""
Stworzyć następujące iteratory nieskończone:
(a) zwracający 0, 1, 0, 1, 0, 1, ...,
(b) zwracający przypadkowo jedną wartość z ("N", "E", "S", "W") [błądzenie przypadkowe na sieci kwadratowej 2D],
(c) zwracający 0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6, ... [numery dni tygodnia].
"""
import itertools
import random

def iter_A():
    return itertools.cycle([0, 1])


def iter_B():
    return (random.choice(("N", "E", "S", "W")) for _ in iter(int, 1))


def iter_C():
    return itertools.cycle(range(7))


if __name__ == "__main__":
    limit = 10

    it_a = iter_A()
    for i, value in enumerate(it_a):
        print(value, end=" ")
        if i > limit:
            break

    print()

    it_b = iter_B()
    for i, value in enumerate(it_b):
        print(value, end=" ")
        if i > limit:
            break
    print()

    it_c = iter_C()
    for i, value in enumerate(it_c):
        print(value, end=" ")
        if i > limit:
            break
