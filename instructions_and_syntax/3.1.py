def test():

    #   Incorrect (C-style)
    # x = 2;
    # y = 3;
    # if (x > y):
    #     result = x;
    # else:
    #     result = y;

    #   Correct
    x = 2
    y = 3
    if x > y:
        result = x
    else:
        result = y

    #   Or
    result = x if x > y else y

    return result


def test2():
    #   Incorrect (only simple statement)
    # for i in "axby": if ord(i) < 100: print(i)

    #   Correct
    for i in 'axby':
        if ord(i) < 100:
            print(i)


def test3():
    #   Incorrect ( multiple statements in one line)
    # for i in "axby": print(ord(i) if ord(i) < 100 else i)

    #   Correct
    for i in "axby":
        print(x if (x := ord(i)) < 100 else i)


def main():
    test()
    test2()
    test3()
