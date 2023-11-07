"""
Napisać iteracyjną wersję funkcji factorial(n) obliczającej silnię.
"""


def factorial(n):
    sum_n = 1
    for i in range(2, n+1):
        sum_n *= i

    return sum_n

def main():
    assert factorial(5) == 120
    assert factorial(1) == 1
    assert factorial(0) == 1
    print('Tests passed!')

if __name__ == '__main__':
    main()