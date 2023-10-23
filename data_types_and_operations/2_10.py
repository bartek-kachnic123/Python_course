"""
Mamy dany napis wielowierszowy line. Podać sposób obliczenia liczby wyrazów
w napisie. Przez wyraz rozumiemy ciąg "czarnych" znaków, oddzielony od innych
wyrazów białymi znakami (spacja, tabulacja, newline).
"""


def count_words(line: str):
    return len(line.split())


def main():
    line = 'some example \n hello world   \t   xyzzz'
    assert count_words(line) == 5
    print("Test passed!")


if __name__ == '__main__':
    main()
