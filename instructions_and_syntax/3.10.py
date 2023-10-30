"""
Stworzyć słownik tłumaczący liczby zapisane w systemie rzymskim
(z literami I, V, X, L, C, D, M) na liczby arabskie
(podać kilka sposobów tworzenia takiego słownika).
Mile widziany kod tłumaczący całą liczbę [funkcja roman2int()].
"""
romanDict = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

romanDict2 = dict(zip(['I', 'V', 'X', 'C', 'D', 'M'], [1, 5, 10, 50, 100, 500, 1000]))

romanDict3 = dict(I=1, V=5, X=50, C=100, D=500, M=1000)


def roman2int(roman_number: str) -> int:
    previous_value = 1001  # more than M
    total_sum = 0
    for char in roman_number:
        current_value = romanDict.get(char)

        if current_value <= previous_value:
            total_sum += current_value
        else:
            total_sum += current_value - (2 * previous_value)
        previous_value = current_value

    return total_sum


def main():
    roman_number = 'XXIV'
    assert roman2int(roman_number) == 24

    roman_number = 'XXXVIII'
    assert roman2int(roman_number) == 38

    roman_number = 'MMCDXLIV'
    assert roman2int(roman_number) == 2444


if __name__ == '__main__':
    main()
