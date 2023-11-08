"""
Rozwiązania zadań 3.5 i 3.6 z poprzedniego zestawu zapisać
w postaci funkcji, które zwracają pełny string przez return.
Funkcje nie powinny pytać użytkownika o dane, tylko korzystać z argumentów.
"""


def make_ruler(n, spacing=5):
    if n <= 0 or spacing <= 0:
        raise ValueError("N and spacing must be postive integers")

    ruler_row = ["{}{}".format('|'.ljust(spacing, '.') * n, '|\n')]

    for num in range(n):
        ruler_row.append('{}{}'.format(num, ' ' * (spacing-len(str(num+1)))))
    ruler_row.append(f'{n}\n')

    return ''.join(ruler_row)


def make_grid(rows, cols):
    if rows <= 0 or cols <= 0:
        raise ValueError('rows and cols must be positive integers')

    grid = ['{}{}'.format('+'.ljust(4, '-') * rows, '+\n'),
            '{}{}'.format('|'.ljust(4, ' ') * rows, '|\n')]

    grid *= cols
    grid.append(grid[0])

    return ''.join(grid)


def main():
    print(make_ruler(10))
    print(make_grid(4, 3))


if __name__ == '__main__':
    main()
