"""
Napisać iteracyjną wersję funkcji fibonacci(n)
obliczającej n-ty wyraz ciągu Fibonacciego.
"""


def fibonacci(n):
    if n == 0 or n == 1:
        return n

    num1 = 0
    num2 = 1
    for i in range(n-1):
        num1, num2 = num2, num1 + num2

    return num2


def main():
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    print("Tests passed!")


if __name__ == '__main__':
    main()
