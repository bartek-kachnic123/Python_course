"""
Zbudować napis stworzony z pierwszych znaków
wyrazów z wiersza line. Zbudować napis
stworzony z ostatnich znaków wyrazów z
wiersza line.
"""


def first_char_line(line: str):
    return ''.join((word[0] for word in line.split()))


def last_char_line(line: str):
    return ''.join((word[-1] for word in line.split()))


def main():
    line = 'some example \n hello world   \t     xyzzz'
    assert first_char_line(line) == 'sehwx'
    assert last_char_line(line) == 'eeodz'
    print("Test passed!")


if __name__ == '__main__':
    main()
