from math import sqrt, ceil


def compute(n, p, g):
    result = None
    x1_values = {}

    A = ceil(sqrt(p-1))

    for i in range(A):
        x1_values[pow(g, i*A, p)] = i

    for x2 in range(A):
        tmp = (n * pow(g, - x2, p)) % p
        if tmp in x1_values:
            x1 = x1_values[tmp]
            result = A * x1 + x2
            break 

    return result


if __name__ == "__main__":
    p = 62076683
    q = 2
    n = 3
    print(compute(n, p, q))