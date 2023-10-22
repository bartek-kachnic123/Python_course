"""
Na liście L mamy liczby jedno-,
dwu- i trzycyfrowe dodatnie. Chcemy zbudować
napis z trzycyfrowych bloków, gdzie liczby
jedno- i dwucyfrowe będą miały blok dopełniony
zerami, np. 007, 024. Wskazówka: str.zfill()
"""


def make_string(L: list):
    return ' '.join((str(x).zfill(3) for x in L))


def main():
    L = [1, 32, 999, 12, 1, 4, 121, 11]
    print(make_string(L))


if __name__ == '__main__':
    main()
