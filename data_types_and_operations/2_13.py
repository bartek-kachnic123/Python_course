"""
Znaleźć łączną długość wyrazów w napisie line.
"""


def count_length_words(line: str):
    return sum((len(word) for word in line.split()))


def main():
    line = 'some example \n hello world   \t     xyzzz'
    print(count_length_words(line))


if __name__ == '__main__':
    main()
