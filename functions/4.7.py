"""
Mamy daną sekwencję, w której niektóre z
elementów mogą okazać się podsekwencjami, a takie zagnieżdżenia mogą
się nakładać do nieograniczonej głębokości. Napisać funkcję
flatten(sequence), która zwróci spłaszczoną listę wszystkich elementów
sekwencji. Wskazówka: rozważyć wersję rekurencyjną, a sprawdzanie
czy element jest sekwencją, wykonać przez isinstance(item, (list, tuple)).
"""


def flatten(seq):
    full_seq = []
    for item in seq:
        if isinstance(item, (list, tuple)):
            full_seq.extend(flatten(item))
        else:
            full_seq.append(item)
    return full_seq

def main():
    seq = [1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]
    print(flatten(seq))  # [1,2,3,4,5,6,7,8,9]


if __name__ == '__main__':
    main()
