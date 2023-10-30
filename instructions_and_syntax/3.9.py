"""
Mamy daną listę sekwencji (listy lub krotki) różnej długości
zawierających liczby. Znaleźć listę zawierającą sumy liczb
z tych sekwencji. Przykładowa sekwencja [[],[4],(1,2),[3,4],(5,6,7)],
spodziewany wynik [0,4,3,7,18]
"""


def sum_inner_list(numbers):
    return [sum(nums) for nums in numbers]


def main():
    numbers = [[], [4], (1, 2), [3, 4], (5, 6, 7)]
    print(sum_inner_list(numbers))


if __name__ == '__main__':
    main()
