"""
Znaleźć: (a) najdłuższy wyraz,
(b) długość najdłuższego wyrazu w napisie line.
"""


def find_longest_word(line: str):
    return max((word for word in line.split()), key=len)


def find_longest_length_word(line: str):
    return max(len(word) for word in line.split())


def main():
    line = 'some example \n hello world   \t     xyzzz'
    assert find_longest_word(line) == 'example'
    assert find_longest_length_word(line) == len('example')


if __name__ == '__main__':
    main()
