"""
W tekście znajdującym się w zmiennej
line zamienić ciąg znaków "GvR" na "Guido van Rossum".
"""


def expand_name(line: str):
    return line.replace('GvR', 'Guido van Rossum')


def main():
    line = 'some example \n hello world  GvR \t    xyzzz'
    line_expanded = 'some example \n hello world  Guido van Rossum \t    xyzzz'
    assert expand_name(line) == line_expanded
    print("Test passed!")


if __name__ == '__main__':
    main()
