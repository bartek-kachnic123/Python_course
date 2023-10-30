"""
Dla dwóch sekwencji liczb lub znaków znaleźć:
(a) listę elementów występujących jednocześnie w obu sekwencjach (bez powtórzeń)
(b) listę wszystkich elementów z obu sekwencji (bez powtórzeń).
"""


def unique_values_intersection(a, b):
    return set(a).intersection(b)


def unique_values_union(a, b):
    return set(a).union(b)


def main():
    a = [1, 2, 3]
    b = [1, 3, 10]
    print(unique_values_intersection(a, b))
    print(unique_values_union(a, b))


if __name__ == '__main__':
    main()
