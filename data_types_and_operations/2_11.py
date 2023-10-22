"""
Podać sposób wyświetlania
napisu word tak, aby jego znaki były rozdzielone znakiem podkreślenia.
"""


def print_with_sep(word: str, sep: str):
    print(*[char for char in word], sep=sep)


def main():
    word = 'word'
    print_with_sep(word, '_')


if __name__ == '__main__':
    main()
