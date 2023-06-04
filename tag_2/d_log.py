from typing import Dict


def find_generator(p: int):
    p = 11
    q = p - 1

    s = (q*(q+1)) // 2

    for g in range(1, p-1):
        elements = []
        for i in range(1, p):
            elements.append(pow(g, i, p))
        if s == sum(elements):
            print(f"{g}: {elements}")
            print(g)


def compute_generator(p: int, g: int) -> Dict:
    elements = {}
    for i in range(1, p):
        elements[pow(g, i, p)] = i

    return elements


def compute_generator_faster(p: int, g: int) -> Dict:
    elements = {}
    res = 1
    for i in range(1, p):
        res = res * g % p
        elements[res] = i

    return elements


# find_generator(11)

g = compute_generator_faster(7, 3)
print(g[5])

g = compute_generator_faster(11, 2)
print(g[7])

g = compute_generator_faster(2696063, 5)
print(g[42])

g = compute_generator_faster(62076683, 2)
print(g[3])
