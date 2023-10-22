"""
Posortować wyrazy z napisu line raz alfabetycznie,
a raz pod względem długości.
"""


def sort(line: str):
    sorted_asc = sorted((word for word in line.split()))
    print(sorted_asc)

    sorted_len = sorted(sorted_asc, key=len, reverse=True)
    print(sorted_len)


def main():
    line = 'some example \n hello world  GvR \t    xyzzz'
    sort(line)


if __name__ == '__main__':
    main()
