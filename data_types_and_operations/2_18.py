"""
Znaleźć liczbę cyfr zero w dużej liczbie całkowitej.
"""


def count_zeros(num: int):

    return str(num).count('0')


def main():
    num = 1232831801
    assert count_zeros(num) == 1
    print("Test passed!")


if __name__ == '__main__':
    main()
