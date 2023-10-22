"""
Na liście L znajdują się liczby całkowite dodatnie.
Stworzyć napis będący ciągiem cyfr kolejnych liczb z
listy L.
"""


def make_string(L: list):
    return ''.join((str(x) for x in L))


def main():
    L = [1, 3, 4, 5, 6, 7]
    assert make_string(L) == '134567'
    print('Test passed')


if __name__ == '__main__':
    main()
