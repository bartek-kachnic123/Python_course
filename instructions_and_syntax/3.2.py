
# 1 Incorrect (two statements in one line)
# L = [3, 5, 4] ; L = L.sort()
# Correct
L = [3, 5, 4]
L = L.sort()

# 2 Incorrect (three values to unpack)
# x, y = 1, 2, 3
# Correct
x, y, z = 1, 2, 3

# 3 Incorrect (Tuples are immutable)
# X = 1, 2, 3 ; X[1] = 4
# Correct
X = (1, 2, 3)

# 4 Incorrect (Index values are in [0, 2]
# X = [1, 2, 3] ; X[3] = 4

# 5 Incorrect (str class doesnt have append func)
# X = "abc" ; X.append("d")

# 6 Incorrect (pow uses min two args)
# L = list(map(pow, range(8)))
# Correct
P = list(map(pow, range(8), (2 for i in range(0, 8))))
