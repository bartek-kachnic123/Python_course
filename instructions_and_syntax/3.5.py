"""
Napisać program rysujący "miarkę" o zadanej długości.
Należy prawidłowo obsłużyć liczby składające się z kilku cyfr
(ostatnia cyfra liczby ma znajdować się pod znakiem kreski pionowej).
Należy zbudować pełny string, a potem go wypisać.
"""


def draw_measure(length: int, spacing: int = 5):
    assert length > 0 and spacing > 0

    measure_string = f'{'|'.ljust(spacing, '.') * length}{'|\n'}'
    numbers_string = ''
    for num in range(length):
        numbers_string += f'{num}{' ' * (spacing-len(str(num+1)))}'
    measure_string += numbers_string + f'{length}\n'
    print(measure_string)


def main():
    draw_measure(15)
    draw_measure(15, 10)
    # measure(1001, 10)


if __name__ == '__main__':
    main()
