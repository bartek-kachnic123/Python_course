"""
Napisać funkcję sum_seq(sequence)
obliczającą sumę liczb zawartych w sekwencji, która może
zawierać zagnieżdżone podsekwencje. Wskazówka: rozważyć wersję
rekurencyjną, a sprawdzanie, czy element jest sekwencją,
wykonać przez isinstance(item, (list, tuple)).
"""


def sum_seq(seq):
    total = 0
    for item in seq:
        if isinstance(item, (list, tuple)):
            total += sum_seq(item)
        else:
            total += item
    return total


def main():
    seq = [1, 2, [3, 2, 1], [3, 3, 3, [1, 2], [1, 2]]]
    assert sum_seq(seq) == 24
    print("Test passed!")


if __name__ == '__main__':
    main()
