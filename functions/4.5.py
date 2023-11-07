"""
Napisać funkcję odwracanie(L, left, right)
odwracającą kolejność elementów na liście od numeru left do right włącznie.
Lista jest modyfikowana w miejscu (in place). Rozważyć wersję iteracyjną i rekurencyjną.
"""


def reverse(L, left, right):
    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1


def reverse_recursive(L, left, right):
    if left >= right:
        return

    L[left], L[right] = L[right], L[left]
    return reverse_recursive(L, left + 1, right - 1)


def main():

    a = [1, 2, 3, 4, 5]
    reverse(a, 2, 4)
    assert a == [1, 2,  5, 4, 3]

    b = [1, 2, 3, 4, 5]
    reverse_recursive(b, 2, 4)
    assert b == [1, 2, 5, 4, 3]

    print("Tests passed!")


if __name__ == '__main__':
    main()
