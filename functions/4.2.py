"""
Rozwiązania zadań 3.5 i 3.6 z poprzedniego zestawu zapisać
w postaci funkcji, które zwracają pełny string przez return.
Funkcje nie powinny pytać użytkownika o dane, tylko korzystać z argumentów.
"""


def make_ruler(n, spacing=5):
    if n <= 0 or spacing <= 0:
        raise ValueError("N and spacing must be postive integers")

    ruler_string = "{}{}".format('|'.ljust(spacing, '.') * n, '|\n')
    numbers_string = ''
    for num in range(n):
        numbers_string += '{}{}'.format(num, ' ' * (spacing-len(str(num+1))))
    ruler_string += numbers_string + f'{n}\n'

    return ruler_string


def make_grid(rows, cols):
    if rows <= 0 or cols <= 0:
        raise ValueError('rows and cols must be positive integers')

    grid_string = '{}{}'.format('+'.ljust(4, '-') * rows, '+\n')
    grid_string += '{}{}'.format('|'.ljust(4, ' ') * rows, '|\n')
    grid_string *= cols
    grid_string += '{}{}'.format('+'.ljust(4, '-') * rows, '+\n')

    return grid_string


def main():
    print(make_ruler(10))
    print(make_grid(4, 3))


if __name__ == '__main__':
    main()
