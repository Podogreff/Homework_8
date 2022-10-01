def sum_of(a, b):
    return a + b


def factor(x):
    f = 1
    for i in range(1, x + 1):
        f *= i
    return f


def reverse_word(a):
    return a[::-1]
