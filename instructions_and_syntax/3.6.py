"""
Napisać program rysujący prostokąt zbudowany z małych kratek.
Należy zbudować pełny string, a potem go wypisać. Przykładowy
prostokąt składający się 2x4 pól ma postać:
"""


def draw_rectangle(width: int, heigth: int):
    assert width > 0 and heigth > 0
    rectangle_string = f'{'+'.ljust(4, '-') * width}{'+\n'}'
    rectangle_string += f'{'|'.ljust(4, ' ') * width}{'|\n'}'
    rectangle_string *= heigth
    rectangle_string += f'{'+'.ljust(4, '-') * width}{'+\n'}'
    
    print(rectangle_string)


def main():
    draw_rectangle(4, 2)
    draw_rectangle(8, 3)


if __name__ == '__main__':
    main()
