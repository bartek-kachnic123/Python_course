"""
Znaleźć liczbę cyfr zero w dużej liczbie całkowitej.
"""


def find_zero(num: int):
    str_num = str(num)
    return str_num.find('0')


def main():
    num = 1232831801
    index = find_zero(num)
    assert str(num)[index] == '0'
    print("Test passed!")


if __name__ == '__main__':
    main()
