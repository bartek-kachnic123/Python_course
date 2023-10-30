"""
Wypisać w pętli liczby od 0 do 30 z wyjątkiem liczb podzielnych przez 3.
"""


def test_for():
    for i in range(0, 31):
        if i % 3 == 0:
            continue
        print(i, end=' ')
        
    print()

def main():
    test_for()


if __name__ == '__main__':
    main()
